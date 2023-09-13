from fastapi import FastAPI

from chapter6.sqlalchemy.database import get_database, sqlalchemy_engine
from chapter6.sqlalchemy.models import (metadata)


app = FastAPI()

# on_event decorator allow us to trigger some useful logic when FastAPI starts or stops
@app.on_event("startup")
async def startup():
    await get_database().connect()
    metadata.create_all(sqlalchemy_engine)


@app.on_event("shutdown")
async def shutdown():
    await get_database().disconnect()
