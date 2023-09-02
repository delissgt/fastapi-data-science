from fastapi import Header, HTTPException, status, FastAPI, Depends
from typing import Optional


def secret_header(secret_header: Optional[str] = Header(None)) -> None:
    if not secret_header or secret_header != "SECRET_VALUE":
        raise HTTPException(status.HTTP_403_FORBIDDEN)

app = FastAPI()


@app.get("/protected-route", dependencies=[Depends(secret_header)])
async def protected_route():
    return {"hello": "word"}
