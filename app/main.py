from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from . import crud, models

app = FastAPI(title="Library Management System - Phase 1")

@app.get("/")
def root() -> dict:
    """
    Health check endpoint for the API.
    """
    return {"status": "OK"}

@app.post("/books")
def create_book(book: models.BookCreate) -> models.Book:
    return crud.create_book(book)

@app.get("/books")
def list_all_books() -> List[models.Book]:
    return crud.list_books()

@app.get("/books/{book_id}")
def get_book(book_id: int) -> models.Book:
    found = crud.get_book(book_id)
    if found is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return found

@app.put("/books/{book_id}")
def update_book(book_id: int, payload: models.BookUpdate) -> models.Book:
    updated = crud.update_book(book_id=book_id, updates=payload)
    if updated is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated

@app.delete("/books/{book_id}")
def delete_book(book_id: int) -> dict:
    ok = crud.delete_book(book_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"status": "OK"}