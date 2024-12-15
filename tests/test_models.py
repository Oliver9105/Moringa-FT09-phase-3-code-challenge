# tests/test_models.py
import pytest
from models.article import Article
from models.author import Author
from models.magazine import Magazine

class TestModels:

    def test_magazine_creation(self):
        # Create a Magazine instance with all required fields
        magazine = Magazine(1, "Tech Weekly", "Technology")
        assert magazine.id == 1
        assert magazine.name == "Tech Weekly"
        assert magazine.category == "Technology"

    def test_author_creation(self):
        # Create an Author instance
        author = Author(1, "John Doe")
        assert author.id == 1
        assert author.name == "John Doe"

    def test_article_creation(self):
        # Create an Article instance
        article = Article(1, "The Future of Tech", "Exploring emerging technologies", 1, 1)
        assert article.id == 1
        assert article.title == "The Future of Tech"
        assert article.content == "Exploring emerging technologies"
        assert article.author_id == 1
        assert article.magazine_id == 1
