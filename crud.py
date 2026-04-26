from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "title": "Book 1",
        "author": "Author 1",
        "price": 100,
        "rating": 4.5
    },
    {
        "title": "Book 2",
        "author": "Author 2",
        "price": 200,
        "rating": 4.2
    },
    {
        "title": "Book 3",
        "author": "Author 3",
        "price": 300,
        "rating": 4.8
    }
]

@app.get("/books")
def get_books():
    return books


# ✅ FIXED PATH PARAMETER
@app.get("/books/{title}")
def get_book_by_title(title: str):
    for book in books:
        if book["title"] == title:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )


class Book(BaseModel):
    title: str
    author: str
    price: float
    rating: float


@app.post("/books")
def create_book(book: Book):
    new_book = book.model_dump()   # convert to dict 
    books.append(new_book)
    return new_book


# Update the data
@app.put('/books/{title}')
def update_book(title: str, updated_book: Book):
    for index, book in enumerate(books):
        if book["title"] == title:
            books[index] = updated_book.model_dump()
            return books[index]

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )

    # Delete

@app.delete("/book/{title}")
def delete_book(title:str):
    for book in books:
        if book['title'] == title:
            books.remove(book)
            return {"message" : "book delete "}

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )
    