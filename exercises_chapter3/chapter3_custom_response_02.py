from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse

app = FastAPI()


@app.get("/redirect")
async def redirect():
    return RedirectResponse("/new-url")


@app.get("/new-url", response_class=HTMLResponse)
async def new_url():
    return """
    <html>
        <head>
            <title>new url</title>
        </head>
        <body>
            <h1>redicto to new_url</h1>
        </body>
    </html>
    """