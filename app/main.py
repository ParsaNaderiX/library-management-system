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

@app.delete("/delete-book/{book_id}")
def delete_book(book_id: int) -> dict:
    if book_id not in books:
        return {"Error": "The book doesn't exist!"}
    
    del books[book_id]
    return {"status": "OK"}

@app.put("/update-book/{book_id}")
def update_book(book_id: int, book_title: str | None = None,
                book_author: str | None = None, book_year: int | None = None,
                book_description: str | None = None) -> dict:
    if book_id not in books:
        return {"Error": "The book doesn't exist!"}
    
    if book_title is not None:
        books[book_id]["title"] = book_title
    if book_author is not None:
        books[book_id]["author"] = book_author
    if book_year is not None:
        books[book_id]["year"] = book_year
    if book_description is not None:
        books[book_id]["description"] = book_description
    
    return {"status": "OK"}