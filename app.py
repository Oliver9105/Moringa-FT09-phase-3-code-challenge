import random
from models.author import Author
from models.magazine import Magazine
from models.article import Article
from database.connection import get_db_connection
from database.setup import create_tables

def main():
    try:
        conn = get_db_connection()
        create_tables()

        # Auto-generate author name
        author_names = ["J.K. Rowling", "George R.R. Martin", "Agatha Christie", "Isaac Asimov", "J.R.R. Tolkien"]
        author_name = random.choice(author_names)
        print(f"Using auto-generated author name: {author_name}")

        magazine_name = input("Enter magazine name: ")
        magazine_category = input("Enter magazine category: ")
        article_title = input("Enter article title: ")

        try:
            author = Author(name=author_name)
        except ValueError as e:
            print(f"Error creating author: {e}")
            return

        try:
            magazine = Magazine(name=magazine_name, category=magazine_category)
        except ValueError as e:
            print(f"Error creating magazine: {e}")
            return

        try:
            article = Article(author=author, magazine=magazine, title=article_title)
        except ValueError as e:
            print(f"Error creating article: {e}")
            return

        print(f"Author: {author.name}, Magazine: {magazine.name}, Article: {article.title}")

        print("Author's Articles:", author.articles())
        print("Author's Magazines:", author.magazines())

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
