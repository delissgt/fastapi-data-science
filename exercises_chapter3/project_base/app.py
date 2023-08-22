from fastapi import FastAPI

from exercises_chapter3.project_base.routers.posts import router as posts_router
from exercises_chapter3.project_base.routers.users import router as users_router

app = FastAPI()

app.include_router(posts_router, prefix="/posts", tags=["posts"])
app.include_router(users_router, prefix="/users", tags=["users"])
