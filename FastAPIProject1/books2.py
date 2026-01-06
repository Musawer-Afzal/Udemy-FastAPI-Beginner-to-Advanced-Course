from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int


    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(description = 'ID is not needed on create', default = None)
    title: str = Field(min_length = 3)
    author: str = Field(min_length = 1)
    description: str = Field(min_length = 1, max_length = 100)
    rating: int = Field(gt = -1, lt = 6)
    published_date: int = Field(gt = 0, lt = 2026)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "chadcoding",
                "description": "A new great book",
                "rating": 5,
                "published_date": 2022
            }
        }
    }




BOOKS = [
    Book(1, 'Computer Science Pro', 'codewithme', 'A book for chads', 5, 2022),
    Book(2, 'Be Fast with FastAPI', 'codewithme', 'A great book', 5, 2011),
    Book(3, 'Master Endpoints', 'codewithme', 'A awesome book', 5, 2020),
    Book(4, 'HP1', 'Author1', 'A wonderful book', 2, 1988),
    Book(5, 'HP2', 'Author2', 'A easy book', 3, 1876),
    Book(6, 'HP3', 'Author3', 'A coding book, Duh', 1, 1999),
]

@app.get("/books")
async def read_all_books():
    return BOOKS


# @app.get("/books/{book_id}")
# async def read_book_by_id(book_id: int = Path(gt = 0)):
#     for book in BOOKS:
#         if book.id == book_id:
#             return book


@app.get("/books/")
async def read_book_by_rating(book_rating: int = Query(gt = 0, lt = 6)):
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

@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book

@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt = 0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break

@app.get("/books/{publised_date}")
async def read_book_by_published_date(published_date: int = Query(gt = 0, lt = 2026)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return