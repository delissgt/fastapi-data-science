from fastapi import FastAPI, status, Depends, HTTPException, Query
from typing import List, Tuple

from databases import Database

from chapter6.sqlalchemy.database import get_database, sqlalchemy_engine
from chapter6.sqlalchemy.models import (metadata, posts, PostDB, PostCreate, PostPartialUpdate)

app = FastAPI()


# on_event decorator allow us to trigger some useful logic when FastAPI starts or stops
@app.on_event("startup")
async def startup():
    await get_database().connect()
    metadata.create_all(sqlalchemy_engine)


@app.on_event("shutdown")
async def shutdown():
    await get_database().disconnect()


# ------
# PAGINATION
async def pagination(skip: int = Query(0, ge=0), limit: int = Query(10, ge=0), ) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)


# GET OR 404
async def get_post_or_404(id: int, database: Database = Depends(get_database)) -> PostDB:
    select_query = posts.select().where(posts.c.id == id)
    raw_post = await database.fetch_one(select_query)

    if raw_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return PostDB(**raw_post)


# ------------
# Query INSERT
@app.post("/posts", response_model=PostDB, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate, database: Database = Depends(get_database)) -> PostDB:
    insert_query = posts.insert().values(post.model_dump())
    post_id = await database.execute(insert_query)
    post_db = await get_post_or_404(post_id, database)
    return post_db


# Query SELECT  - list objects
@app.get("/posts")
async def list_posts(
        pagination: Tuple[int, int] = Depends(pagination),
        database: Database = Depends(get_database),
) -> List[PostDB]:
    skip, limit = pagination
    select_query = posts.select().offset(skip).limit(limit)
    rows = await database.fetch_all(select_query)

    results = [PostDB(**row) for row in rows]

    return results


# Query SELECT - get a object
@app.get("/posts{id}", response_model=PostDB)
async def get_post(post: PostDB = Depends(get_post_or_404)) -> PostDB:
    return post
