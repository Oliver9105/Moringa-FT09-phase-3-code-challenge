import sqlite3
from models.author import Author
from models.magazine import Magazine
from models.article import Article
from database.connection import get_db_connection
from database.setup import create_tables

def main():
    try:
        conn = get_db_connection()
        create_tables()

        # Get user input for author, magazine, and article details
        while True:
            author_name = input("Enter author name: ")
            if author_name.strip():  # Check if author name is not empty after removing leading/trailing spaces
                break
            print("Author name cannot be empty. Please enter a valid name.")

        while True:
            magazine_name = input("Enter magazine name: ")
            if magazine_name.strip():  # Check if magazine name is not empty after removing leading/trailing spaces
                break
            print("Magazine name cannot be empty. Please enter a valid name.")

        magazine_category = input("Enter magazine category: ")
        article_title = input("Enter article title: ")
        article_content = input("Enter article content: ")

        try:
            author = Author.create_author(author_name)
        except ValueError as e:
            print(f"Error creating author: {e}")
            return

        try:
            magazine = Magazine.create_magazine(magazine_name, magazine_category)
        except ValueError as e:
            print(f"Error creating magazine: {e}")
            return

        try:
            article = Article(author=author, magazine=magazine, title=article_title)
            article.content = article_content
            article.save()  # Save the article to the database
        except ValueError as e:
            print(f"Error creating article: {e}")
            return

        print(f"Author: {author.name}, Magazine: {magazine.name}, Article: {article.title}")

        # Assuming author.articles() and author.magazines() are implemented in the Author class
        try:
            print("Author's Articles:", author.articles())
        except Exception as e:
            print(f"Error retrieving author's articles: {e}")

        try:
            print("Author's Magazines:", author.magazines())
        except Exception as e:
            print(f"Error retrieving author's magazines: {e}")

        # Print contributing authors for the magazine
        try:
            contributing_authors = magazine.contributing_authors()
            print("Contributing Authors (more than 2 articles):")
            for author in contributing_authors:
                print(f"- {author[1]}")  # Assuming the second column in the result is the author's name
        except Exception as e:
            print(f"Error retrieving contributing authors: {e}")

    except sqlite3.Error as db_error:
        print(f"Database error: {db_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        conn.close()

def display_magazine_authors_and_articles(magazine_name):
    conn = sqlite3.connect('database/magazine.db')
    cursor = conn.cursor()
    query = '''
    SELECT 
        authors.name AS author_name, articles.title AS article_title
    FROM 
        articles
    JOIN 
        authors ON articles.author_id = authors.id
    JOIN 
        magazines ON articles.magazine_id = magazines.id
    WHERE 
        magazines.name = ?
    '''
    cursor.execute(query, (magazine_name,))
    results = cursor.fetchall()
    conn.close()

    print(f"Magazine: {magazine_name}")
    if results:
        print("Authors and their Articles:")
        for idx, (author_name, article_title) in enumerate(results, start=1):
            print(f"{idx}. {author_name} - \"{article_title}\"")
    else:
        print("No articles found for this magazine.")

if __name__ == "__main__":
    main()
