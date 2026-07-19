import os
import re
import ast
import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI
from sqlalchemy import text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import database engine and utilities
from database import engine, normalize_ident

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- 1. VECTOR DB CHROMA CLIENT ---
import chromadb
from chromadb.utils import embedding_functions

try:
    db_path = os.path.join(BASE_DIR, "chroma_db")
    chroma_client = chromadb.PersistentClient(path=db_path)
    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.getenv("OPENAI_API_KEY"),
        model_name="text-embedding-3-small"
    )
    collection = chroma_client.get_or_create_collection(
        name="schema_fields",
        embedding_function=openai_ef,
        metadata={"hnsw:space": "cosine"}
    )
except Exception as e:
    print(f"Warning: Could not connect to Chroma DB. {e}")
    collection = None

# --- 2. API CLIENTS INITIALIZATION ---
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



# --- 3. AGENT TOOLS (The Hands) ---

def find_most_similar(query_text, table_filter=None, top_k=5, viz_type=""):
    """
    TOOL 1: Semantic Schema Search using Chroma DB (OpenAI Embeddings)
    """
    if not collection:
        return "Chroma DB not initialized."

    if viz_type == "map" and "geometry" not in str(query_text).lower():
        if query_text and str(query_text).lower() != "none":
            print(f"   [System] 'Map' detected. Injecting geometry keywords into search.")
            query_text = str(query_text) + " geometry polygon boundary shapefile FIPS code"
        elif str(query_text).lower() == "none" or not query_text:
            query_text = "geometry polygon boundary shapefile FIPS code"

    print(f"   [Tool] Searching Chroma Schema for '{query_text}' (Filter: {table_filter})...")
    
    try:
        where_filter = None
        if table_filter:
            where_filter = {"Table": table_filter}

        res = collection.query(
            query_texts=[query_text],
            n_results=top_k,
            where=where_filter
        )

        # If table_filter was used but returned nothing, fallback to global search
        if table_filter and (not res or not res["ids"] or len(res["ids"][0]) == 0):
            print(f"   [System] Table '{table_filter}' fallback query...")
            fallback_query = f"{query_text} {table_filter}"
            res = collection.query(
                query_texts=[fallback_query],
                n_results=top_k
            )

        if not res or not res["ids"] or len(res["ids"][0]) == 0:
            return "No matches found in vector DB."

        results = []
        for idx in range(len(res["ids"][0])):
            meta = res["metadatas"][0][idx]
            dist = res["distances"][0][idx] if res["distances"] else 1.0
            score = 1.0 - dist # Cosine similarity score

            results.append(
                f"Score: {score:.4f} | Table: {meta['Table']} | Column: {meta['Column Name']} | "
                f"Type: {meta['Data Type']} | Desc: {meta['Description']}"
            )
        return "\n".join(results)
    except Exception as e:
        return f"Chroma Search Error: {e}"

def get_table_metadata(table_name):
    """
    TOOL 2: Technical Table Schema Inspection
    """
    print(f"   [Tool] Inspecting schema for '{table_name}'...")
    if not collection:
        return "Chroma DB not initialized."

    try:
        res = collection.get(where={"Table": table_name})
        metadatas = res.get("metadatas", [])
        if not metadatas:
            return "Table not found in metadata."
        
        columns = []
        for meta in metadatas:
            col_name = meta['Column Name']
            dtype = meta['Data Type']
            
            # Smart Quoting for Case Sensitivity
            if not re.match(r"^[a-z0-9_]+$", col_name):
                 col_name = f'"{col_name}"'
            
            columns.append(f"{col_name}({dtype})")
            
        return ", ".join(columns)
    except Exception as e:
        return f"Error reading schema metadata: {e}"

def check_value_in_db(table, column, value):
    """
    TOOL 3: Database Value Grounding
    """
    print(f"   [Tool] Checking DB for value '{value}' in {table}.{column}...")
    try:
        tbl = normalize_ident(table)
        col = normalize_ident(column)
        sql_query = f"SELECT DISTINCT {col} FROM {tbl} WHERE {col}::text ILIKE :like_val LIMIT 5"

        with engine.connect() as conn:
            df = pd.read_sql_query(text(sql_query), conn, params={"like_val": f"%{value}%"})

        if df.empty: 
            return "Query executed successfully. No results found."
        
        actual_values = df.iloc[:, 0].tolist()
        return f"Match Found! The exact values in the database are: {actual_values}"

    except Exception as e:
        return f"SQL Execution Error: {str(e)}"

def run_query_sandbox(sql_query, viz_type="", user_question=""):
    """
    TOOL 4: TEST_SQL (Sandbox execution with warnings)
    """
    if re.search(r"\b(DROP|DELETE|UPDATE|INSERT|ALTER)\b", sql_query, re.IGNORECASE):
        return "Error: Sandbox only allows SELECT queries."

    try:
        with engine.connect() as conn:
            df = pd.read_sql_query(text(sql_query), conn)
        
        row_count = len(df)
        if row_count == 0:
            return "Query executed successfully, but returned 0 rows."
        
        warnings = []
        
        if viz_type in ["map", "chart"] and row_count == 1:
            warnings.append(
                "[SYSTEM WARNING]: You returned only 1 row for a Map/Chart. "
                "Did you forget to GROUP BY (e.g., by County or Year)? "
                "Maps/Charts need multiple data points."
            )
            
        if viz_type == "map":
            has_geoid = any(str(col).lower() == "geoid" for col in df.columns)
            has_geom = any(str(col).lower() in ['geometry', 'geom', 'shape', 'wkb_geometry'] for col in df.columns)
            if not has_geoid:
                warnings.append(
                    "[SYSTEM WARNING]: User asked for a MAP, but result has no GEOID column. "
                    "Return one identifier column aliased exactly as 'geoid'."
                )
            if has_geom:
                warnings.append(
                    "[SYSTEM WARNING]: For MAP queries, do NOT return geometry in SQL output. "
                    "Return only 'geoid' + metric columns."
                )
            if has_geoid:
                geoid_col = next((c for c in df.columns if str(c).lower() == "geoid"), None)
                if geoid_col is not None:
                    geoid_sample = (
                        df[geoid_col]
                        .dropna()
                        .astype(str)
                        .str.strip()
                        .head(50)
                        .tolist()
                    )
                    if geoid_sample:
                        invalid_geoid_count = sum(1 for v in geoid_sample if len(v) not in (2, 5, 11))
                        if invalid_geoid_count > 0:
                            warnings.append(
                                "[SYSTEM WARNING]: The `geoid` values do not look like canonical GEOIDs "
                                "(expected lengths: 2=state, 5=county, 11=tract). "
                                "Do NOT alias `statefp`/`countyfp`/`tractce` as `geoid`; use the actual "
                                "lowercase `geoid` column from boundary/data tables."
                            )
        elif viz_type == "chart":
            q = str(user_question or "").lower()
            wants_scatter = "scatter" in q or "correlation" in q
            if wants_scatter:
                identifier_names = {"geoid", "state", "state_name", "county", "county_name", "name", "year"}
                numeric_cols = []
                for col in df.columns:
                    col_name = str(col).strip()
                    if col_name.lower() in identifier_names:
                        continue
                    numeric_series = pd.to_numeric(df[col], errors="coerce")
                    if numeric_series.notna().any():
                        numeric_cols.append(col_name)
                if len(numeric_cols) < 2:
                    warnings.append(
                        "[SYSTEM WARNING]: Scatter plot requires TWO numeric variables. "
                        "Return at least two numeric columns (e.g., x_value and y_value), "
                        "plus optional identifier."
                    )
        
        preview_df = df.head(5)
        
        null_msg = ""
        if preview_df.isnull().values.any():
            null_msg = "\n[SYSTEM NOTE]: Result contains NULL values. Consider filtering with 'IS NOT NULL'."
            
        warning_str = "\n".join(warnings)
        if warning_str:
            warning_str = "\n\n" + warning_str
            
        return f"Query returned {row_count} rows. Sandbox Preview:\n{preview_df.to_string(index=False)}{null_msg}{warning_str}"

    except Exception as e:
        return f"SQL Execution Error: {str(e)}"

def execute_final_sql(sql_query, limit=8000):
    """
    TOOL 5: Final query execution
    """
    sql_query = sql_query.strip().rstrip(";")
    sql_query_limited = f"SELECT * FROM ({sql_query}) q LIMIT {limit}"
    with engine.connect() as conn:
        df = pd.read_sql_query(text(sql_query_limited), conn)
    return df


# --- 4. REFLECTIVE AGENT IMPLEMENTATION ---

class HealthAgent:
    def __init__(self):
        self.history = []
        self.client = openai_client

    def call_openai(self, system_prompt, messages):
        try:
            full_messages = [{"role": "system", "content": system_prompt}] + messages
            response = self.client.chat.completions.create(
                model="gpt-4o-2024-05-13",
                messages=full_messages,
                response_format={"type": "json_object"},
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI API Error: {e}")
            return None

    def clean_json_response(self, response_text):
        if response_text is None: 
            return None
        clean_text = response_text.strip()
        if clean_text.startswith("```"):
            clean_text = clean_text.split("\n", 1)[1]
            if clean_text.endswith("```"):
                clean_text = clean_text.rsplit("\n", 1)[0]
        return clean_text

    def run(self, context_json):
        user_question = context_json.get("Question")
        viz_type = context_json.get("Visualization", "")
        level = context_json.get("Level", "")

        print(f"--- NEW GOAL: {user_question} ---")
        print(f"--- CONTEXT: Viz='{viz_type}' | Level='{level}' ---")
        
        self.history = [{"role": "user", "content": user_question}]
        
        step = 0
        max_steps = 30
        
        while step < max_steps:
            step += 1
            print(f"\n--- Step {step} ---")
            
            system_prompt = f"""
            You are an autonomous SQL Agent. You Scout, Hypothesize, and Test.

            CONTEXT:
            - Visualization Needed: {viz_type}
            - Geographic Level: {level}
            - List of tables avialble in the database: 
            "cdc_county_2025": "CDC PLACES health estimates (e.g., diabetes, obesity, depression) aggregated at the County level."
            "cdc_tract_2025": "CDC PLACES health estimates aggregated at the Census Tract level."
            "cdc_zipcode_2025": "CDC PLACES health estimates aggregated at the Zip Code (ZCTA) level."
            "edu_attain_pop_25plus": "Educational attainment data (e.g., degrees earned) for the population aged 25 and over."
            "sex_occ_civemp_pop_16plus": "Breakdown of occupation and employment status by sex for the civilian population aged 16+."
            "school_enroll_level_pop_3plus": "School enrollment statistics by level (nursery through graduate school) for population aged 3+."
            "huseholds_and_families": "Demographic data regarding household types, family structures, and living arrangements."
            "hh_inc_rent_pct_inc_12mo": "Household income data and gross rent as a percentage of household income."
            "employment_status": "General employment metrics including labor force participation and unemployment rates."
            "hlthins_cov_chars_us": "Health insurance coverage characteristics for the US population."
            "pubassist_inc_12mo_hh": "Data on households receiving public assistance income or food stamps/SNAP in the past 12 months."
            "means_of_transportation_to_work": "Commuting data describing how workers travel to their jobs (e.g., car, transit, walk)."
            "aidsvu_county_newdiagnoses": "New HIV/AIDS diagnosis rates and counts by county, stratified by demographics."
            "segregation_index": "Metrics quantifying residential segregation within geographic areas."
            "block_groups": "Geographic boundaries and geometry definitions for Census Block Groups."
            "census_tracts": "Geographic boundaries and geometry definitions for Census Tracts."
            "counties": "Geographic boundaries, FIPS codes, and geometry definitions for US Counties."
            "states": "Geographic boundaries, FIPS codes, and geometry definitions for US States."

            TOOLS:
            1. LOOKUP_SCHEMA(query, table_filter=None): 
            - Search tables semantically. Set table_filter to null to find new tables.
            
            2. INSPECT_TABLE(table_name): 
            - Returns column names. 
            - **CRITICAL**: If output is `"Col"`, you MUST use `"Col"`. If output is `col`, use `col`.
            
            3. CHECK_VALUE(table, column, value):
            - Check exact values for names.
            
            4. TEST_SQL(sql_query): 
            - Executes SQL. Returns Preview + Warnings.
            
            5. FINAL_ANSWER(sql_query): 
            - Final output.

            CRITICAL RULES:
            1. CLEAN ID & HIERARCHY (NEW):
               - **JOIN STRATEGY**: To join a detailed table (e.g. Tract 11-digit) to a County table (5-digit),
                 use `SUBSTRING(detailed_col, 1, 5) = county_col`.
               - For map queries, always return one identifier column aliased exactly as `geoid`.
               - In `states`, `counties`, and `census_tracts`, use the real lowercase `geoid` column.
               - NEVER alias `statefp`, `countyfp`, or `tractce` as `geoid`.

            2. VISUALIZATION & DATA CONTEXT:
               - If Viz='both': return `geoid` + metric columns required for both the map and chart (e.g., a geographic identifier column aliased as `geoid`, the map metric column, and the chart relationship metric columns). Never select geometry columns.
               - If Viz='map': return `geoid` + data columns (e.g. 'Rate', 'Percentage').
               - For map queries, NEVER SELECT geometry columns in the final output.
               - JOIN with boundary tables (`counties`, `states`) only to align identifiers.
               - If user asks heatmap/heat map, still return `geoid` + numeric weight column.
               - If Viz='chart': the output MUST NOT return geometry. It should return identifier and data columns. The output should include that geographic identifier (For State and County name and for other levels id).
               - If user asks for scatter/scatter plot/correlation: return TWO numeric measure columns for X and Y (e.g., `obesity_rate`, `depression_rate`) plus optional identifier column.

            3. AGGREGATION & CASTING:
               - Many data columns are TEXT. **ALWAYS** use `::numeric` for math.
               - Example: `AVG("Rate"::numeric)`.

            4. SIMPLICITY:
               - **DO NOT** use `WITH` clauses (CTEs). Use standard `JOIN` and `GROUP BY`.

            OUTPUT FORMAT (JSON):
            {{"thought": "...", "tool": "TEST_SQL", "args": ["..."]}}
            """
            
            response_text = self.call_openai(system_prompt, self.history)
            if not response_text: 
                break

            try:
                clean_text = self.clean_json_response(response_text)
                action = json.loads(clean_text)
                print(f"Thought: {action.get('thought')}")
                yield f"{action.get('thought')}"
                print(f"Action:  {action.get('tool')}")
            except Exception as e:
                print(f"Error parsing JSON: {e}")
                break

            tool_name = action.get('tool')
            args = action.get('args', [])
            tool_output = "No output"
            
            # --- TOOL EXECUTION ---
            if tool_name == "TEST_SQL":
                tool_output = run_query_sandbox(args[0], viz_type=viz_type, user_question=user_question)
            
            elif tool_name == "FINAL_ANSWER":
                final_sql = args[0]
                print(f"\n>>> MISSION SUCCESS. VERIFIED SQL:\n{final_sql}")
                yield f"Final SQL Query:\n{final_sql}\n"
                try:
                    result_df = execute_final_sql(final_sql)
                    print(">>> Execution Successful.")
                    yield f"Final query executed successfully."
                    yield {"final_result": result_df} 
                except Exception as e:
                    print(f"\n>>> FINAL EXECUTION ERROR: {e}")
                    yield f"I faced an error executing final SQL: {e}"
                    result_df = final_sql
                
                return result_df

            elif tool_name == "LOOKUP_SCHEMA":
                q = args[0] if len(args) >= 1 else user_question
                t_filter = args[1] if len(args) > 1 else None
                tool_output = find_most_similar(str(q), table_filter=t_filter, viz_type=viz_type)
                
            elif tool_name == "INSPECT_TABLE":
                tool_output = get_table_metadata(args[0])
                
            elif tool_name == "CHECK_VALUE":
                if len(args) == 3:
                    tool_output = check_value_in_db(args[0], args[1], args[2])
                else:
                    tool_output = "Error: CHECK_VALUE requires 3 args [table, column, value]"
            
            else:
                tool_output = f"Error: Unknown tool '{tool_name}'"

            safe_output = str(tool_output)[:2000]
            print(f"   [Tool Output] {safe_output[:500]}...")
            
            self.history.append({"role": "assistant", "content": response_text})
            self.history.append({"role": "user", "content": f"Tool Output: {safe_output}"})
        
        return "Error: Agent timed out or failed to produce a query."
