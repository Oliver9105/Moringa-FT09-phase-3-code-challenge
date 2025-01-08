import sqlite3

class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = None
        self.name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("id must be of type int")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value

    def _validate_name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")

    @classmethod
    def create_author(cls, name):
        conn = sqlite3.connect('database/magazine.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO authors (name)
        VALUES (?)
        ''', (name,))
        conn.commit()
        id = cursor.lastrowid
        conn.close()
        return cls(id, name)

    def articles(self):
        conn = sqlite3.connect('database/magazine.db')
        cursor = conn.cursor()
        query = """
        SELECT articles.*
        FROM articles
        JOIN authors ON articles.author_id = authors.id
        WHERE authors.id = ?
        """
        cursor.execute(query, (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def magazines(self):
        conn = sqlite3.connect('database/magazine.db')
        cursor = conn.cursor()
        query = """
        SELECT DISTINCT magazines.*
        FROM magazines
        JOIN articles ON magazines.id = articles.magazine_id
        JOIN authors ON articles.author_id = authors.id
        WHERE authors.id = ?
        """
        cursor.execute(query, (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines
