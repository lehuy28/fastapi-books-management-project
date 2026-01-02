from fastapi import FastAPI
from app.api.endpoints import authors, books, categories
from fastapi.staticfiles import StaticFiles


#static flies

app = FastAPI(
    title = "Book Management API",
    description = " Simple API to manage books, authors, categories and book covers ",
    version = "1.0.0"
)
#include routers

app.include_router(authors.router, prefix="/authors", tags=["authors"])
app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(categories.router, prefix="/categories", tags=["categories"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Management API"}