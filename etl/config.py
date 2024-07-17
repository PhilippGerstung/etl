import pathlib as pl

DATA_ROOT = (pl.Path(__file__).parents[2] / "data").resolve()
DUCKDB_PATH = DATA_ROOT / "gpv.db"

stations_csv_file_path = DATA_ROOT / "stations/2024/07/2024-07-10-stations.csv"
