import unittest
from models.magazine import Magazine
from models.author import Author
from models.article import Article

class TestModels(unittest.TestCase):

    def test_magazine_creation(self):
        # Create a Magazine instance with all required fields
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.id, 1)
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

    def test_author_creation(self):
        # Create an Author instance
        author = Author(1, "John Doe")
        self.assertEqual(author.id, 1)
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        # Create an Article instance
        article = Article(1, "The Future of Tech", "Exploring emerging technologies", 1, 1)
        self.assertEqual(article.id, 1)
        self.assertEqual(article.title, "The Future of Tech")
        self.assertEqual(article.content, "Exploring emerging technologies")
        self.assertEqual(article.author_id, 1)
        self.assertEqual(article.magazine_id, 1)

if __name__ == '__main__':
    unittest.main()
