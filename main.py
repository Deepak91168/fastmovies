from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
conn = MongoClient("mongodb+srv://ds9210048:ds9210048@cluster0.otmffrq.mongodb.net/")

try:
    conn.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = conn['sample_mflix']  # Use your database name ('sample_mflix')
collection = db['movies'] 

# Fetch 10 movies from the 'movies' collection
movies = collection.find().limit(10)

# Convert MongoDB cursor to a list of dictionaries
movie_list = list(movies)
print(movie_list)
# for movie in movie_list:
#     print(movie)

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    movies = collection.find().limit(5)
    movie_list = list(movies)
    return templates.TemplateResponse("index.html", {"request": request, "items": movie_list})


