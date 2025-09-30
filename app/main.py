from fastapi import FastAPI

books = {}

app = FastAPI()

@app.get("/health")
def health() -> dict:
    return {"status": "OK"}

@app.post("/add-book")
def add_book(book_id: int, book_title: str, book_author: str,
                book_year: int, book_description: str | None = None) -> dict:
    if book_id in books:
        return {"Error": "We already have the book!"}
    
    books[book_id] = {"title": book_title, "author": book_author,
                        "year": book_year, "description": book_description}
    return {"status": "OK"}

@app.get("/get-book/{book_id}")
def get_book(book_id: int) -> dict:
    if book_id not in books:
        return {"Error": "We don't have the book!"}
    
    return books[book_id]