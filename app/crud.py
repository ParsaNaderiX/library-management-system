from typing import Dict, List, Optional
from .models import Book, BookCreate

# In-memory database (keyed by book id for O(1) access)
books_db: Dict[int, Book] = {}
book_id_counter = 1

def create_book(book: BookCreate) -> Book:
    global book_id_counter
    new_book = Book(
        id=book_id_counter,
        title=book.title,
        author=book.author,
        year=book.year,
        description=book.description,
    )

    books_db[new_book.id] = new_book
    book_id_counter += 1
    return new_book

def list_books() -> List[Book]:
    return list(books_db.values())

def get_book(book_id: int) -> Optional[Book]:
    return books_db.get(book_id)

def update_book(
    book_id: int,
    title: Optional[str] = None,
    author: Optional[str] = None,
    year: Optional[int] = None,
    description: Optional[str] = None,
) -> Optional[Book]:
    existing = books_db.get(book_id)
    if existing is None:
        return None

    updated = existing.model_copy(update={
        "title": title if title is not None else existing.title,
        "author": author if author is not None else existing.author,
        "year": year if year is not None else existing.year,
        "description": description if description is not None else existing.description,
    })
    books_db[book_id] = updated
    return updated

def delete_book(book_id: int) -> bool:
    if book_id in books_db:
        del books_db[book_id]
        return True
    return False