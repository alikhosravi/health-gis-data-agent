import os
import json
import gzip
from threading import Lock
import pandas as pd
import geopandas as gpd
from shapely import wkb
from sqlalchemy import text
from flask import Flask, request, jsonify, render_template, Response, stream_with_context

# Import database connection and the Health Agent
from database import engine, normalize_ident
from health_agent import HealthAgent

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

GEOMETRY_CACHE_TABLES = ("states", "counties", "census_tracts")
GEOMETRY_CACHE_VERSION = "2026-02-12-v1"
_GEOMETRY_CACHE_PAYLOAD = None
_GEOMETRY_CACHE_LOCK = Lock()

MAP_HINT_KEYWORDS = (
    " map",
    "map ",
    "heatmap",
    "heat map",
    "choropleth",
    "geospatial",
    "spatial",
)

CHART_HINT_KEYWORDS = (
    "chart",
    "plot",
    "line graph",
    "bar chart",
    "pie chart",
    "scatter",
    "scatter plot",
    "correlation",
    "trend",
    "time series",
)


# --- 1. FRONTEND ROUTING HELPERS ---

def is_geometry_column(series, sample_size=3):
    sample = series.dropna().head(sample_size)
    try:
        for v in sample:
            wkb.loads(v, hex=True)
        return True
    except Exception:
        return False

def infer_request_context(question):
    lower = str(question or "").lower()
    viz_type = ""

    has_map = any(k in lower for k in MAP_HINT_KEYWORDS)
    has_chart = any(k in lower for k in CHART_HINT_KEYWORDS)

    if has_map and has_chart:
        viz_type = "both"
    elif has_map:
        viz_type = "map"
    elif has_chart:
        viz_type = "chart"

    level = ""
    if "block group" in lower or "block_group" in lower:
        level = "block_groups"
    elif "tract" in lower:
        level = "census_tracts"
    elif "county" in lower or "counties" in lower:
        level = "counties"
    elif "state" in lower:
        level = "states"

    return {"Question": question, "Visualization": viz_type, "Level": level}

def find_geoid_column(columns):
    for col in columns:
        if str(col).lower() == "geoid":
            return col
    for col in columns:
        if "geoid" in str(col).lower():
            return col
    return None

def get_geometry_columns(df):
    geometry_name_hints = {"geometry", "geom", "shape", "wkb_geometry"}
    geom_cols = []
    for col in df.columns:
        if str(col).lower() in geometry_name_hints or is_geometry_column(df[col]):
            geom_cols.append(col)
    return geom_cols

def build_map_payload_from_geoid(df):
    geoid_col = find_geoid_column(df.columns)
    if geoid_col is None:
        return None

    map_df = df.copy()
    if geoid_col != "geoid":
        map_df = map_df.rename(columns={geoid_col: "geoid"})

    map_df = map_df[map_df["geoid"].notna()].copy()
    map_df["geoid"] = map_df["geoid"].astype(str).str.strip()
    map_df = map_df[map_df["geoid"] != ""].copy()

    geom_cols = get_geometry_columns(map_df)
    if geom_cols:
        map_df = map_df.drop(columns=geom_cols, errors="ignore")

    return {
        "Mode": "GeoidRows",
        "GeoidColumn": "geoid",
        "Rows": json.loads(map_df.to_json(orient="records")),
    }


# --- 2. BOUNDARY GEOMETRY CACHING ---

def load_geometry_cache_payload():
    datasets = {}
    with engine.connect() as conn:
        for table in GEOMETRY_CACHE_TABLES:
            tbl = normalize_ident(table)
            cache_geom_col = "geom_simplified" if table == "census_tracts" else "geometry"
            geom_col = normalize_ident(cache_geom_col)
            sql = text(
                f"""
                SELECT geoid::text AS geoid, ST_AsGeoJSON({geom_col}) AS geometry_json
                FROM {tbl}
                WHERE geoid IS NOT NULL AND {geom_col} IS NOT NULL
                """
            )
            rows = []
            for geoid, geometry_json in conn.execute(sql):
                if geoid is None or geometry_json is None:
                    continue
                try:
                    geometry = json.loads(geometry_json) if isinstance(geometry_json, str) else geometry_json
                except Exception:
                    continue
                rows.append({"geoid": str(geoid), "geometry": geometry})
            datasets[table] = rows
            print(f"[GeometryCache] Loaded {len(rows)} geometries from '{table}'.")

    return {"Version": GEOMETRY_CACHE_VERSION, "Datasets": datasets}

def get_geometry_cache_payload():
    global _GEOMETRY_CACHE_PAYLOAD
    if _GEOMETRY_CACHE_PAYLOAD is not None:
        return _GEOMETRY_CACHE_PAYLOAD

    with _GEOMETRY_CACHE_LOCK:
        if _GEOMETRY_CACHE_PAYLOAD is None:
            _GEOMETRY_CACHE_PAYLOAD = load_geometry_cache_payload()
    return _GEOMETRY_CACHE_PAYLOAD


# --- 3. FLASK SERVER ROUTES ---

@app.route("/")
def index():
    return render_template("index.html", openai_api_key=os.getenv("OPENAI_API_KEY", ""))


@app.route("/geometry-cache", methods=["GET"])
def geometry_cache():
    payload = get_geometry_cache_payload()
    raw_json = json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    accept_encoding = request.headers.get("Accept-Encoding", "").lower()

    if "gzip" in accept_encoding:
        gzipped = gzip.compress(raw_json, compresslevel=6)
        response = Response(gzipped, mimetype="application/json")
        response.headers["Content-Encoding"] = "gzip"
        response.headers["Vary"] = "Accept-Encoding"
        response.headers["Content-Length"] = str(len(gzipped))
        response.headers["X-Uncompressed-Length"] = str(len(raw_json))
        return response

    return Response(raw_json, mimetype="application/json")

@app.route("/information", methods=["POST"])
def ask_question():
    data = request.get_json()
    question = data.get("question")
    context = infer_request_context(question)
    
    def generate():
        agent = HealthAgent()
        generator = agent.run(context)
        
        final_data = None
        
        for item in generator:
            if isinstance(item, dict) and "final_result" in item:
                final_data = item["final_result"]
            else:
                yield json.dumps({"Type": "Log", "Data": str(item)}) + "\n"
        
        if final_data is not None:
            if isinstance(final_data, str):
                yield json.dumps({"Type": "Text", "Data": final_data}) + "\n"
            else:
                df = final_data
                viz_mode = context.get("Visualization")

                if viz_mode == "both":
                    # Build and stream Map payload
                    geoid_payload = build_map_payload_from_geoid(df)
                    if geoid_payload is not None:
                        yield json.dumps({"Data": geoid_payload, "Type": "Map"}) + "\n"

                    # Build and stream Chart/Table payload (filtering out geom columns)
                    chart_df = df.copy()
                    geom_cols = get_geometry_columns(chart_df)
                    if geom_cols:
                        chart_df = chart_df.drop(columns=geom_cols, errors="ignore")
                    yield json.dumps({
                        "Data": json.loads(chart_df.to_json(orient="records")),
                        "Type": "Chart or Table"
                    }) + "\n"
                    return

                if viz_mode == "map":
                    geoid_payload = build_map_payload_from_geoid(df)
                    if geoid_payload is not None:
                        payload = {"Data": geoid_payload, "Type": "Map"}
                        yield json.dumps(payload) + "\n"
                        return

                geom_cols = get_geometry_columns(df)
                if len(geom_cols) > 0:
                    df["geometry"] = df[geom_cols[0]].apply(lambda x: wkb.loads(x, hex=True))
                    gdf = gpd.GeoDataFrame(df, geometry="geometry", crs="EPSG:4326")
                    payload = {"Data": json.loads(gdf.to_json()), "Type": "Map"}
                else:
                    payload = {
                        "Data": json.loads(df.to_json(orient="records")),
                        "Type": "Chart or Table"
                    }
                yield json.dumps(payload) + "\n"
        else:
            yield json.dumps({"Type": "Text", "Data": "No result returned from agent."}) + "\n"

    return Response(stream_with_context(generate()), mimetype='application/x-ndjson')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4042)

