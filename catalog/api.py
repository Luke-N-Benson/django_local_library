from .models import Author, Genre, Language
from ninja import NinjaAPI, ModelSchema
from ninja.orm import create_schema

api = NinjaAPI()

AuthorSchema = create_schema(Author, fields=['first_name', 'last_name', 'date_of_birth', 'date_of_death'])

GenreSchema = create_schema(Genre, fields=['name'])

LanguageSchema = create_schema(Language, fields=['name'])

from django.shortcuts import get_object_or_404
from typing import List

@api.post("/authors")
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

@api.put("/authors/{author_id}")
def update_author(request, author_id: int, payload: AuthorSchema):
    author = get_object_or_404(Author, id=author_id)
    for attr, value in payload.dict().items():
        setattr(author, attr, value)
    author.save()
    return {"success": True}

@api.delete("/authors/{author_id}")
def delete_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    author.delete()
    return {"success": True}

@api.post("/genres")
def create_genre(request, payload: GenreSchema):
    genre = Genre.objects.create(**payload.dict())
    return {"id": genre.id}

@api.get("/genres/{genre_id}", response=GenreSchema)
def get_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    return genre

@api.put("/genres/{genre_id}")
def update_genre(request, genre_id: int, payload: GenreSchema):
    genre = get_object_or_404(Genre, id=genre_id)
    for attr, value in payload.dict().items():
        setattr(genre, attr, value)
    genre.save()
    return {"success": True}

@api.get("/genres", response=List[GenreSchema])
def list_genres(request):
    qs = Genre.objects.all()
    return qs

@api.delete("/genres/{genre_id}")
def delete_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    genre.delete()
    return {"success": True}

@api.post("/languages")
def create_language(request, payload: LanguageSchema):
    language = Language.objects.create(**payload.dict())
    return {"id": language.id}

@api.get("/lanaguages", response=List[LanguageSchema])
def list_languages(request):
    qs = Language.objects.all()
    return qs

@api.get("/languages/{language_id}", response=LanguageSchema)
def get_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    return language

@api.put("/languages/{language_id}")
def update_language(request, language_id: int, payload: LanguageSchema):
    language = get_object_or_404(Language, id=language_id)
    for attr, value in payload.dict().items():
        setattr(language, attr, value)
    language.save()
    return {"success": True}

@api.delete("/languages/{language_id}")
def delete_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    language.delete()
    return {"success": True}