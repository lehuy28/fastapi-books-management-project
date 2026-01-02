from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import models for Alembic - using lazy import to avoid circular imports
# These imports should only be used by Alembic's env.py
def import_models():
    from app.models.author import Author
    from app.models.book import Book
    from app.models.category import Category
    return Author, Book, Category