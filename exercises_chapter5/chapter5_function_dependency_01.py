from fastapi import FastAPI, Depends

from typing import Tuple

app = FastAPI()

# DEFINE A DEPENDECY FUNCTION TO RETRIEVE THE PAGINATION QUERY PARAMETERS, SKIP AND LIMIT
async def pagination(skip: int = 0, limit: int = 10) -> Tuple[int, int]:
    return skip, limit


# THE PATH FUNCTION list_items USES THE pagitation DEPENDENCY
@app.get("/items")
async def list_items(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}


@app.get("/things")
async def list_things(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}

