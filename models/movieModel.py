from pydantic import BaseModel

class MovieModel(BaseModel):
    title: str
    description: str
