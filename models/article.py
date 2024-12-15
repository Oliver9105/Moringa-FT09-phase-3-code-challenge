# models/article.py
class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id


    def create_article(self):
        cursor = self.connection.cursor()
        query = "INSERT INTO articles (author_id, magazine_id, title) VALUES (?, ?, ?)"
        cursor.execute(query, (self.author.id, self.magazine.id, self.title))
        self.connection.commit()
        self.id = cursor.lastrowid  # Fetch the last inserted row's id
