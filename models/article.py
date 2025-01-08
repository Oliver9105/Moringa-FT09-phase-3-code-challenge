import sqlite3

class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self.title = title
        self.content = None
        self._id = None  # Initialize the id attribute

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = value 

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if value is not None and not isinstance(value, str):
            raise ValueError("Content must be a string or None")
        self._content = value

    def save(self):
        conn = sqlite3.connect('database/magazine.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO articles (title, content, author_id, magazine_id)
            VALUES (?, ?, ?, ?)
        ''', (self.title, self.content, self._author.id, self._magazine.id))
        conn.commit()
        self._id = cursor.lastrowid  # Get the ID of the newly inserted row
        conn.close()

    def update_content_in_db(self):
        if not self._id:
            raise ValueError("Article must be saved before updating content.")
        conn = sqlite3.connect('database/magazine.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE articles
            SET content = ?
            WHERE id = ?
        ''', (self.content, self._id))
        conn.commit()
        conn.close()

    @property
    def author(self):
        from models.author import Author  # Late import to avoid circular dependency
        conn = sqlite3.connect('database/magazine.db')
        cursor = conn.cursor()
        query = """
        SELECT authors.*
        FROM authors
        JOIN articles ON authors.id = articles.author_id
        WHERE articles.id = ?
        """
        cursor.execute(query, (self._id,))
        author_data = cursor.fetchone()
        conn.close()
        if author_data:
            return Author(author_data[0], author_data[1])
        return None

    @property
    def magazine(self):
        from models.magazine import Magazine  # Late import to avoid circular dependency
        conn = sqlite3.connect('database/magazine.db')
        cursor = conn.cursor()
        query = """
        SELECT magazines.*
        FROM magazines
        JOIN articles ON magazines.id = articles.magazine_id
        WHERE articles.id = ?
        """
        cursor.execute(query, (self._id,))
        magazine_data = cursor.fetchone()
        conn.close()
        if magazine_data:
            return Magazine(magazine_data[0], magazine_data[1], magazine_data[2])
        return None
