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
