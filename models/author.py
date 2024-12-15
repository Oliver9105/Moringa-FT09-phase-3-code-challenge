# models/author.py
class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name


    def create_author(self, name):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
        self.connection.commit()
        self.id = cursor.lastrowid  # Fetch the last inserted row's id
        self.name = name
