from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int


    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(description = 'ID is not needed on create', default = None)
    title: str = Field(min_length = 3)
    author: str = Field(min_length = 1)
    description: str = Field(min_length = 1, max_length = 100)
    rating: int = Field(gt = -1, lt = 6)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "chadcoding",
                "description": "A new great book",
                "rating": 5
            }
        }
    }




BOOKS = [
    Book(1, 'Computer Science Pro', 'codewithme', 'A book for chads', 5),
    Book(2, 'Be Fast with FastAPI', 'codewithme', 'A great book', 5),
    Book(3, 'Master Endpoints', 'codewithme', 'A awesome book', 5),
    Book(4, 'HP1', 'Author1', 'A wonderful book', 2),
    Book(5, 'HP2', 'Author2', 'A easy book', 3),
    Book(6, 'HP3', 'Author3', 'A coding book, Duh', 1),
]

@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}")
async def read_book_by_id(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book


@app.get("/books/")
async def read_book_by_rating(book_rating: int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    # Efficient code
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    return book