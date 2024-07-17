import duckdb

from etl import config

# Connect to the DuckDB database (this will create the file if it doesn't exist)
con = duckdb.connect(config.DUCKDB_PATH.as_posix())

# Load the CSV file into a DuckDB table
con.execute(
    f"""
    CREATE TABLE IF NOT EXISTS stations AS SELECT * FROM read_csv_auto('{config.stations_csv_file_path.as_posix()}');
"""
)

con.commit()
# Close the connection
con.close()
