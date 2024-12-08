from author import Author
from magazine import Magazine
from article import Article

# Create objects
author = Author("John Doe")
magazine = Magazine("Tech Weekly", "Technology")
article = Article(author, magazine, "The Future of AI")

# Test methods
print(author.articles())
print(magazine.contributors())
print(author.topic_areas())
