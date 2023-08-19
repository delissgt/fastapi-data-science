from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
async def custom_header(response: Response):
    response.headers["Custom-Header"] = "Custom-Header-Value-Deliss"
    # return {"hello": "word"}
