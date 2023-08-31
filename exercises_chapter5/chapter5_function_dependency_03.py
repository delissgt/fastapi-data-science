from typing import Dict, Optional

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    content: str


class PostUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]


class DummyDatabase:
    posts: Dict[int, Post] = {}


db = DummyDatabase()
db.posts = {
    1: Post(id=1, title="Post 1", content="Content 1"),
    2: Post(id=2, title="Post 2", content="Content 2"),
    3: Post(id=3, title="Post 3", content="Content 3"),
}


app = FastAPI()

# TODO implementing : Get object or raise 404 error
async def get_post_or_404(id: int) -> Post:
    try:
        return db.posts[id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

#Authentication dependency cookie
@app.get("/posts/{id}")
async def get(post: Post = Depends(get_post_or_404)):
    return post


#Authentication dependency cookie
@app.patch("/posts/{id}")
async def update(post_update: PostUpdate, post: Post = Depends(get_post_or_404)):
    updated_post = post.model_copy(update=post_update.model_dump())
    db.posts[post.id] = updated_post
    return updated_post


#Authentication dependency cookie
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(post: Post = Depends(get_post_or_404)):
    db.posts.pop(post.id)
