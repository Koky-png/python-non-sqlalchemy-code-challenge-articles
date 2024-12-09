import pytest
from classes.many_to_many import Article, Magazine, Author


class TestMagazine:
    def test_has_name(self):
        """Magazine is initialized with a name."""
        magazine = Magazine("Vogue", "Fashion")
        assert magazine.name == "Vogue"

    def test_invalid_name(self):
        """Magazine raises ValueError for invalid names."""
        with pytest.raises(ValueError):
            Magazine("", "Fashion")
        with pytest.raises(ValueError):
            Magazine(123, "Fashion")

    def test_has_category(self):
        """Magazine is initialized with a category."""
        magazine = Magazine("Vogue", "Fashion")
        assert magazine.category == "Fashion"

    def test_invalid_category(self):
        """Magazine raises ValueError for invalid categories."""
        with pytest.raises(ValueError):
            Magazine("Vogue", "")
        with pytest.raises(ValueError):
            Magazine("Vogue", 123)

    def test_has_many_articles(self):
        """Magazine can have multiple articles."""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")
        assert len(magazine.articles()) == 2
        assert article_1 in magazine.articles()
        assert article_2 in magazine.articles()

    def test_articles_are_of_type_article(self):
        """Magazine articles are of type Article."""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        Article(author, magazine, "Dating life in NYC")
        assert all(isinstance(article, Article) for article in magazine.articles())

    def test_has_many_contributors(self):
        """Magazine has many contributors."""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_2, magazine, "Dating life in NYC")
        assert len(magazine.contributors()) == 2
        assert author_1 in magazine.contributors()
        assert author_2 in magazine.contributors()

    def test_contributors_are_unique(self):
        """Magazine contributors are unique."""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        Article(author, magazine, "How to be single and happy")
        assert len(set(magazine.contributors())) == len(magazine.contributors())

    def test_article_titles(self):
        """Returns list of article titles for the magazine."""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        assert magazine.article_titles() == ["How to wear a tutu with style"]

    def test_contributing_authors(self):
        """Returns authors with more than 2 articles for the magazine."""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_1, magazine, "How to be single and happy")
        Article(author_1, magazine, "Dating life in NYC")
        Article(author_2, magazine, "Carrara Marble is so 2020")
        assert author_1 in magazine.contributing_authors()
        assert author_2 not in magazine.contributing_authors()
