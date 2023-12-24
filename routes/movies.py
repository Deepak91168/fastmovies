from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from config.db import movie_list,collection
from models.movieModel import MovieModel
from schemas.movie import Movie
movie = APIRouter()

templates = Jinja2Templates(directory="templates")

@movie.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    movies = collection.find().limit(10)
    movie_list = list(movies)
    return templates.TemplateResponse("index.html", {"request": request, "items": movie_list})

@movie.post("/")
async def add_movie(request: Request):
    form = await request.form()
    movie = MovieModel(title=form.get('title'), description=form.get('description'))
    movie_dict = movie.dict()
    
    result = collection.insert_one(movie_dict)
    if result.inserted_id:
        return {"message": f"Movie '{movie.title}' added to the database!"}
    else:
        return {"message": "Failed to add movie to the database."}
