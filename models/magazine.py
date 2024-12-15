# models/magazine.py
class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category


    def create_magazine(self, name, category):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
        self.connection.commit()
        self.name = name
        self.category = category
        self.id = cursor.lastrowid
