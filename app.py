
import sqlite3
from models.author import Author
from models.magazine import Magazine
from models.article import Article

def main():
    # Connect to a persistent database file (e.g., database.db)
    conn = sqlite3.connect('database.db')  # Database file will be created here

    # Create tables if they don't exist (you might need to update this based on your schema)
    conn.execute('''CREATE TABLE IF NOT EXISTS authors (id INTEGER PRIMARY KEY, name TEXT)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS magazines (id INTEGER PRIMARY KEY, name TEXT, category TEXT)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS articles (id INTEGER PRIMARY KEY, title TEXT, content TEXT, author_id INTEGER, magazine_id INTEGER)''')

    # Get input from user
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")

    # Create an Author instance and insert into DB
    author = Author(id=1, name=author_name)
    conn.execute("INSERT INTO authors (id, name) VALUES (?, ?)", (author.id, author.name))

    # Create a Magazine instance and insert into DB
    magazine = Magazine(id=1, name=magazine_name, category=magazine_category)
    conn.execute("INSERT INTO magazines (id, name, category) VALUES (?, ?, ?)", (magazine.id, magazine.name, magazine.category))

    # Prompt for article content
    article_content = input("Enter article content: ")

    # Create an Article instance and insert into DB
    article = Article(id=1, title=article_title, content=article_content, author_id=1, magazine_id=1)
    conn.execute("INSERT INTO articles (id, title, content, author_id, magazine_id) VALUES (?, ?, ?, ?, ?)", 
                 (article.id, article.title, article.content, article.author_id, article.magazine_id))

    # Commit the transaction to save data
    conn.commit()

    # Output
    print(f"Author: {author.name}, Magazine: {magazine.name}, Article: {article.title}")

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
