import os
import sys
import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Read environment keys from the local .env
load_dotenv(os.path.join(BASE_DIR, ".env"))

def main():
    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        print("Error: OPENAI_API_KEY not found in environment variables. Please check your .env file.")
        sys.exit(1)

    schema_csv_path = os.path.join(BASE_DIR, "schema.csv")
    if not os.path.exists(schema_csv_path):
        print(f"Error: schema.csv not found at {schema_csv_path}")
        sys.exit(1)

    print("Loading schema.csv...")
    df = pd.read_csv(schema_csv_path)
    
    # Ensure standard schema columns
    required_cols = ["Table", "Column Name", "Data Type", "Description"]
    for col in required_cols:
        if col not in df.columns:
            print(f"Error: Required column '{col}' is missing from schema.csv.")
            sys.exit(1)

    # Initialize Chroma Client
    db_path = os.path.join(BASE_DIR, "chroma_db")
    print(f"Initializing Chroma PersistentClient at {db_path}...")
    chroma_client = chromadb.PersistentClient(path=db_path)

    # Setup OpenAI Embedding Function
    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
        api_key=openai_key,
        model_name="text-embedding-3-small"
    )

    # Recreate the collection to ensure starting fresh
    collection_name = "schema_fields"
    print(f"Recreating collection '{collection_name}'...")
    try:
        chroma_client.delete_collection(collection_name)
    except Exception:
        pass

    collection = chroma_client.create_collection(
        name=collection_name,
        embedding_function=openai_ef,
        metadata={"hnsw:space": "cosine"}
    )

    # Allow running on a specific table for testing/development
    target_table = None
    if len(sys.argv) > 1:
        if sys.argv[1] in ["--help", "-h"]:
            print("Usage: python schema_profiling.py [table_name]")
            sys.exit(0)
        target_table = sys.argv[1]
        df = df[df["Table"] == target_table]
        print(f"Filtering schema profiling to table '{target_table}' ({len(df)} rows)...")

    if df.empty:
        print("No metadata records found to index.")
        return

    print("Preparing documents for Chroma DB indexing...")
    ids = []
    documents = []
    metadatas = []

    for idx, row in df.iterrows():
        table = str(row["Table"])
        column = str(row["Column Name"])
        dtype = str(row["Data Type"])
        desc = str(row["Description"]) if pd.notna(row["Description"]) else ""

        # Unique ID for the record
        ids.append(f"{table}.{column}")
        
        # Semantic text to be embedded (concatenating table details for better matching)
        doc_text = f"Table: {table} | Column: {column} | Type: {dtype} | Description: {desc}"
        documents.append(doc_text)
        
        # Associated metadata fields
        metadatas.append({
            "Table": table,
            "Column Name": column,
            "Data Type": dtype,
            "Description": desc
        })

    # Insert in batches to avoid database size/payload transaction limits
    batch_size = 100
    print(f"Indexing {len(documents)} schema fields into Chroma DB...")
    for i in range(0, len(documents), batch_size):
        end = i + batch_size
        collection.add(
            ids=ids[i:end],
            documents=documents[i:end],
            metadatas=metadatas[i:end]
        )
        print(f"Indexed batch {i // batch_size + 1}/{((len(documents) - 1) // batch_size) + 1}...")

    print("Schema profiling completed successfully.")

if __name__ == "__main__":
    main()
