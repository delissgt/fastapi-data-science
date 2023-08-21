from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse, HTMLResponse

app = FastAPI()


@app.get("/redirect")
async def redirect():
    return RedirectResponse("new-url", status_code=status.HTTP_301_MOVED_PERMANENTLY)


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