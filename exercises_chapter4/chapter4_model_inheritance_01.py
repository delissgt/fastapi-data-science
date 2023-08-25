from pydantic import BaseModel


class PostCreate(BaseModel):
    user: int
    title: str


class Post(BaseModel):
    id: int
    user: int
    title: str


class PostDB(BaseModel):
    id: int
    title: str
    content: str
    nb_views: int = 0

