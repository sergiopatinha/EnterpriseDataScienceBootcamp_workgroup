import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def load_df(name: str, folder: str = "interim") -> pd.DataFrame:
    """
    Load a previously saved DataFrame from the data directory.

    Parameters
    ----------
    name : str
        File name without extension.
    folder : str, optional
        Subfolder inside /data where the file is stored
        (default: "interim").

    Returns
    -------
    pd.DataFrame
        Loaded DataFrame.
    """
    file_path = DATA_DIR / folder / f"{name}.csv"
    df = pd.read_csv(file_path)
    print(f"📂 Loaded: {file_path}")
    return df



def save_df(
    df: pd.DataFrame,
    name: str,
    folder: str = "interim",
    fmt: str = "csv",
    index: bool = False
) -> Path:
    """
    Save a DataFrame to the data directory in a standardized format.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to be saved.
    name : str
        File name (without extension).
    folder : str, optional
        Subfolder inside /data where the file will be saved (default: 'interim').
        Common options: 'raw', 'interim', 'processed'.
    fmt : {'csv', 'parquet'}, optional
        File format to use for saving. Default is 'parquet' (preferred for performance and schema preservation).
    index : bool, optional
        Whether to include the index in the saved file. Default is False.

    Returns
    -------
    Path
        Full path to the saved file.
    """
    folder_path = DATA_DIR / folder
    folder_path.mkdir(parents=True, exist_ok=True)

    file_path = folder_path / f"{name}.{fmt}"

    if fmt == "parquet":
        df.to_parquet(file_path, index=index)
    elif fmt == "csv":
        df.to_csv(file_path, index=index)
    else:
        raise ValueError("Unsupported format. Use 'csv' or 'parquet'.")

    print(f"✅ DataFrame saved to: {file_path}")
    return file_path



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
