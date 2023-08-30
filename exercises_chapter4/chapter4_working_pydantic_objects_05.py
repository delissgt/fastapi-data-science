from typing import Optional, Dict
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status


class PostBase(BaseModel):
    title: str
    content: str


class PostPartialUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class PostCreate(PostBase):
    pass


class PostPublic(PostBase):
    id: int


class PostDB(PostBase):
    id: int
    nb_views: int = 0


class DummyDatabase:
    posts: Dict[int, PostDB] = {}


db = DummyDatabase()

app = FastAPI()


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=PostPublic)
async def create(post_create: PostCreate):
    new_id = max(db.posts.keys() or (0,)) + 1

    post = PostDB(id=new_id, **post_create.model_dump())

    db.posts[new_id] = post
    print("POST", post)
    return post  # omits this returned data and only sends response_model data


# TODO IMPLEMENTING PATCH ENDPOINT
@app.patch("/posts/{id}", response_model=PostPublic)
async def partial_update(id: int, post_update: PostPartialUpdate):
    try:
        post_db = db.posts[id]

        updated_fields = post_update.model_dump(exclude_unset=True)

        updated_post = post_db.model_copy(update=updated_fields)

        db.posts[id] = updated_post
        return updated_post

    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
