import sqlite3

class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self._name = None
        self._category = None
        self.name = name
        self.category = category

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

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._validate_category(value)
        self._category = value

    def _validate_name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")

    def _validate_category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")

    @classmethod
    def create_magazine(cls, name, category):
        conn = sqlite3.connect('database/magazine.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO magazines (name, category)
        VALUES (?, ?)
        ''', (name, category))
        conn.commit()
        id = cursor.lastrowid
        conn.close()
        return cls(id, name, category)

    def articles(self):
        conn = sqlite3.connect('database/magazine.db')
        cursor = conn.cursor()
        query = """
        SELECT articles.*
        FROM articles
        JOIN magazines ON articles.magazine_id = magazines.id
        WHERE magazines.id = ?
        """
        cursor.execute(query, (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def contributors(self):
        conn = sqlite3.connect('database/magazine.db')
        cursor = conn.cursor()
        query = """
        SELECT authors.*
        FROM authors
        JOIN articles ON authors.id = articles.author_id
        JOIN magazines ON articles.magazine_id = magazines.id
        WHERE magazines.id = ?
        """
        cursor.execute(query, (self.id,))
        contributors = cursor.fetchall()
        conn.close()
        return contributors

    def article_titles(self):
        conn = sqlite3.connect('database/magazine.db')
        cursor = conn.cursor()
        query = """
        SELECT articles.title
        FROM articles
        JOIN magazines ON articles.magazine_id = magazines.id
        WHERE magazines.id = ?
        """
        cursor.execute(query, (self.id,))
        titles = cursor.fetchall()
        conn.close()
        return [title[0] for title in titles] if titles else None

    def contributing_authors(self):
        conn = sqlite3.connect('database/magazine.db')
        cursor = conn.cursor()
        query = """
        SELECT authors.*
        FROM authors
        JOIN articles ON authors.id = articles.author_id
        JOIN magazines ON articles.magazine_id = magazines.id
        WHERE magazines.id = ?
        GROUP BY authors.id
        HAVING COUNT(articles.id) > 2
        """
        cursor.execute(query, (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return authors if authors else []
