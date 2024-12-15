import sqlite3
from models.author import Author
from models.magazine import Magazine
from models.article import Article
from database.connection import get_db_connection

def create_tables():
    conn = get_db_connection()

    # Create the necessary tables
    conn.execute('''CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY,
        name TEXT)''')

    conn.execute('''CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT)''')

    conn.execute('''CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY,
        author_id INTEGER,
        magazine_id INTEGER,
        title TEXT,
        FOREIGN KEY (author_id) REFERENCES authors(id),
        FOREIGN KEY (magazine_id) REFERENCES magazines(id))''')

    conn.commit()
    conn.close()
