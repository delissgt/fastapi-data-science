from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/")
async def header(user_agent: str = Header(...)):
    print("user-agent----", user_agent)
    return {"user_agent": Header(user_agent)}
