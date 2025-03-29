from .models import Author, Genre, Language, Book, BookInstance
from ninja import NinjaAPI, Schema
from ninja.orm import create_schema
from ninja.security import django_auth

api = NinjaAPI()

AuthorSchema = create_schema(Author, fields=['first_name', 'last_name', 'date_of_birth', 'date_of_death'])

GenreSchema = create_schema(Genre, fields=['name'])

LanguageSchema = create_schema(Language, fields=['name'])

BookSchema = create_schema(Book, depth=1, fields=['title', 'author', 'genre', 'language'])

BookInstanceSchema = create_schema(BookInstance, depth=1, fields=['id', 'book', 'imprint', 'due_back', 'borrower'])

from django.shortcuts import get_object_or_404
from typing import List

@api.post("/authors", auth=django_auth)
def create_author(request, payload: AuthorSchema):
    author = Author.objects.create(**payload.dict())
    return {"id": author.id}

@api.get("/authors/{author_id}", response=AuthorSchema)
def get_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    return author

@api.get("/authors", response=List[AuthorSchema])
def list_authors(request):
    qs = Author.objects.all()
    return qs

@api.put("/authors/{author_id}", auth=django_auth)
def update_author(request, author_id: int, payload: AuthorSchema):
    author = get_object_or_404(Author, id=author_id)
    for attr, value in payload.dict().items():
        setattr(author, attr, value)
    author.save()
    return {"success": True}

@api.delete("/authors/{author_id}", auth=django_auth)
def delete_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    author.delete()
    return {"success": True}



@api.post("/genres", auth=django_auth)
def create_genre(request, payload: GenreSchema):
    genre = Genre.objects.create(**payload.dict())
    return {"id": genre.id}

@api.get("/genres/{genre_id}", response=GenreSchema)
def get_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    return genre

@api.get("/genres", response=List[GenreSchema])
def list_genres(request):
    qs = Genre.objects.all()
    return qs

@api.put("/genres/{genre_id}", auth=django_auth)
def update_genre(request, genre_id: int, payload: GenreSchema):
    genre = get_object_or_404(Genre, id=genre_id)
    for attr, value in payload.dict().items():
        setattr(genre, attr, value)
    genre.save()
    return {"success": True}

@api.delete("/genres/{genre_id}", auth=django_auth)
def delete_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    genre.delete()
    return {"success": True}



@api.post("/languages", auth=django_auth)
def create_language(request, payload: LanguageSchema):
    language = Language.objects.create(**payload.dict())
    return {"id": language.id}

@api.get("/languages/{language_id}", response=LanguageSchema)
def get_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    return language

@api.get("/languages", response=List[LanguageSchema])
def list_languages(request):
    qs = Language.objects.all()
    return qs

@api.put("/languages/{language_id}", auth=django_auth)
def update_language(request, language_id: int, payload: LanguageSchema):
    language = get_object_or_404(Language, id=language_id)
    for attr, value in payload.dict().items():
        setattr(language, attr, value)
    language.save()
    return {"success": True}

@api.delete("/languages/{language_id}", auth=django_auth)
def delete_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    language.delete()
    return {"success": True}


@api.post("/books", auth=django_auth)
def create_book(request, payload: BookSchema):
    book = Book.objects.create(**payload.dict())
    return {"id": book.id}

@api.get("/books/{book_id}", response=BookSchema)
def get_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return book

@api.get("/books", response=List[BookSchema])
def list_books(request):
    qs = Book.objects.all()
    return qs

@api.put("/books/{book_id}", auth=django_auth)
def update_book(request, book_id: int, payload: BookSchema):
    book = get_object_or_404(Book, id=book_id)
    for attr, value in payload.dict().items():
        setattr(book, attr, value)
    book.save()
    return {"success": True}

@api.delete("/books/{book_id}", auth=django_auth)
def delete_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return {"success": True}



@api.post("/bookinstances", auth=django_auth)
def create_bookinst(request, payload: BookInstanceSchema):
    bookinst = BookInstance.objects.create(**payload.dict())
    return {"id": bookinst.id}

@api.get("/bookinstances/{bookinst_id}", response=BookInstanceSchema)
def get_bookinst(request, bookinst_id: int):
    bookinst = get_object_or_404(BookInstance, id=bookinst_id)
    return bookinst

@api.get("/bookinstances", response=List[BookInstanceSchema])
def list_bookinsts(request):
    qs = BookInstance.objects.all()
    return qs

@api.put("/bookinstances/{bookinst_id}", auth=django_auth)
def update_bookinst(request, bookinst_id: int, payload: BookInstanceSchema):
    bookinst = get_object_or_404(BookInstance, id=bookinst_id)
    for attr, value in payload.dict().items():
        setattr(bookinst, attr, value)
    bookinst.save()
    return {"success": True}

@api.delete("/bookinstances/{bookinst_id}", auth=django_auth)
def delete_bookinst(request, bookinst_id: int):
    bookinst = get_object_or_404(BookInstance, id=bookinst_id)
    bookinst.delete()
    return {"success": True}