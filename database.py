import os
import re
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- 1. DATABASE CONFIGURATION ---
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "user": os.getenv("DB_USER", "bigdata_local"),
    "port": int(os.getenv("DB_PORT", 5432)),
    "password": os.getenv("DB_PASSWORD", "1201"),
    "database": os.getenv("DB_NAME", "Health")
}

DB_URI = (
    f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

engine = create_engine(
    DB_URI,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
)


# --- 2. SQL IDENTIFIER SANITIZATION ---
_SAFE_IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")

def normalize_ident(name: str) -> str:
    if not name: 
        raise ValueError("Identifier cannot be empty")
    name = str(name).strip()
    if not _SAFE_IDENT.match(name): 
        return '"' + name.replace('"', '""') + '"'
    return name
