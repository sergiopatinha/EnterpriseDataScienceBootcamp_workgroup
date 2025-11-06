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






def quick_overview(df: pd.DataFrame, name: str, show_head: bool = True, n_head: int = 5):
    """Print a concise overview of a DataFrame: shape, dtypes, and missing values."""
    print(f"\n===== {name} =====")
    print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")
    print("Data types:")
    print(df.dtypes)
    print("\nMissing values per column:")
    print(df.isna().sum().sort_values(ascending=False))
    if show_head:
        print(f"\nFirst {n_head} rows:")
        display(df.head(n_head))
