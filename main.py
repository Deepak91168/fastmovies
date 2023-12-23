from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from config.db import movie_list,collection

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="templates")

# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     movies = collection.find().limit(5)
#     movie_list = list(movies)
#     return templates.TemplateResponse("index.html", {"request": request, "items": movie_list})


