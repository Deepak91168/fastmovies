from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from config.db import movie_list,collection

movie = APIRouter()

templates = Jinja2Templates(directory="templates")

@movie.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    movies = collection.find().limit(10)
    movie_list = list(movies)
    return templates.TemplateResponse("index.html", {"request": request, "items": movie_list})
0
@movie.post("/")
async def add_movie(request: Request, movie_data: dict):
    movie_id = collection.insert_one(movie_data).inserted_id
    return {"message": "Movie added successfully", "movie_id": str(movie_id)}
