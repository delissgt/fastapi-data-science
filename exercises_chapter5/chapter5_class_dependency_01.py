from fastapi import FastAPI, Depends, Query

from typing import Tuple

app = FastAPI()


# #IMPROVED FUNCTION DEPENDENCY PAGINATION
# TODO Reimplement the pagination with a class, allowing to set maximum limit dynamically
# async def pagination(skip: int = Query(0, ge=0), limit: int = Query(10, ge=0)) -> Tuple[int, int]:
#     capped_limit = min(100, limit)
#     return skip, capped_limit

class Pagination:
    def __init__(self, maximum_limit: int = 100):
        self.maximum_limit = maximum_limit

    async def __call__(
            self,
            skip: int = Query(0, ge=0),
            limit: int = Query(10, ge=0),
                       ) -> Tuple[int, int]:
        capped_limit = min(self.maximum_limit, limit)
        return skip, capped_limit

# create instance of the class Pagination and use it, we set maximum_limit = 50
pagination = Pagination(maximum_limit=50)


# using the instance with "Depends" in the path function
@app.get("/items")
async def list_items(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}


@app.get("/things")
async def list_things(p: Tuple[int, int] = Depends(pagination)):
    skip, limit = p
    return {"skip": skip, "limit": limit}

