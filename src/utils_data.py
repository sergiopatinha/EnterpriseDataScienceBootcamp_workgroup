<<<<<<< HEAD
from pathlib import Path
import pandas as pd
import json
from typing import Literal

# Safe fallback in case __file__ is not available (e.g. running in a notebook)
try:
    ROOT = Path(__file__).resolve().parents[1]
except NameError:
    ROOT = Path(".").resolve().parent

DATA = ROOT / "data"
RAW = DATA / "raw"
INTERIM = DATA / "interim"
PROCESSED = DATA / "processed"

def save_df(df: pd.DataFrame, name: str, stage: Literal["raw", "interim", "processed"] = "interim", fmt: str = "parquet"):
    folder = {"raw": RAW, "interim": INTERIM, "processed": PROCESSED}[stage]
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{name}.{fmt}"

    if fmt == "parquet":
        df.to_parquet(path, index=False)
    elif fmt == "csv":
        df.to_csv(path, index=False)
    elif fmt == "feather":
        df.to_feather(path)
    else:
        raise ValueError("Unsupported file format")

    print(f"✅ Saved {name} → {path}")
    return path

def load_df(name: str, stage: Literal["raw", "interim", "processed"] = "interim"):
    folder = {"raw": RAW, "interim": INTERIM, "processed": PROCESSED}[stage]
    for ext in ("parquet", "feather", "csv"):
        path = folder / f"{name}.{ext}"
        if path.exists():
            if ext == "parquet":
                return pd.read_parquet(path)
            elif ext == "feather":
                return pd.read_feather(path)
            elif ext == "csv":
                return pd.read_csv(path)
    raise FileNotFoundError(f"{name} not found in {folder}")

def save_meta(obj: dict, name: str, stage: str = "processed"):
    folder = {"raw": RAW, "interim": INTERIM, "processed": PROCESSED}[stage]
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{name}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    print(f"💾 Saved metadata → {path}")
    return path

def list_datasets(stage: str = "interim"):
    folder = {"raw": RAW, "interim": INTERIM, "processed": PROCESSED}[stage]
    if not folder.exists():
        return []
    return sorted([f.name for f in folder.iterdir() if f.is_file()])
=======
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def save_df(df: pd.DataFrame, name: str, folder: str = "interim"):
    """Guarda um dataframe como CSV em data/<folder>"""
    folder_path = DATA_DIR / folder
    folder_path.mkdir(parents=True, exist_ok=True)
    file_path = folder_path / f"{name}.csv"
    df.to_csv(file_path, index=False)
    print(f"✅ Guardado: {file_path}")

def load_df(name: str, folder: str = "interim") -> pd.DataFrame:
    """Carrega um dataframe guardado anteriormente"""
    file_path = DATA_DIR / folder / f"{name}.csv"
    df = pd.read_csv(file_path)
    print(f"📂 Carregado: {file_path}")
    return df
>>>>>>> caa416ae9300bf4ff4f712dc4aceb9ceda10b116
