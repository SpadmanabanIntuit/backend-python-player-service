import csv
import sqlite3
import pandas as pd

def import_csv_to_sqlite(csv_file, db_file, table_name):
    """Imports data from a CSV file into an SQLite database table."""

    # Read CSV into a DataFrame
    df = pd.read_csv(csv_file)

    # Create a connection to the SQLite database
    conn = sqlite3.connect(db_file)

    # Write DataFrame to SQLite table
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    import_csv_to_sqlite("Player.csv", "player.db", "players")