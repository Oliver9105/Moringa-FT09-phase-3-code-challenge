import sqlite3

DATABASE_NAME = './database/magazine.db'

def get_db_connection(db_path=None):
    """Establish a connection to the SQLite database."""
    # Use the provided database path or fall back to the default
    db_path = db_path or DATABASE_NAME
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Allows row access by column name
    return conn
