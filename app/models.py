from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    description: Optional[str] = None

class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    description: Optional[str] = None

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    description: Optional[str] = None