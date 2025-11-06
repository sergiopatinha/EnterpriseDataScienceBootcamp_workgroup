# src/config.py
from pathlib import Path

# Root of the project (one folder above src)
ROOT = Path(__file__).resolve().parents[1]

# Data folders
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"
