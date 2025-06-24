from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, JSONResponse
from app.logger import log_request
from app.version import get_git_hash, PROJECT_NAME
import uvicorn
import os
import argparse

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    log_request(request, response)
    return response

@app.get("/helloworld")
async def hello(name: str = None):
    if name:
        formatted_name = name.replace("_", " ").replace("-", " ").title().replace(" ", "")
        return PlainTextResponse(f"Hello {formatted_name}")
    return PlainTextResponse("Hello World")

@app.get("/versionz")
async def versionz():
    return JSONResponse(content={
        "project": PROJECT_NAME,
        "git_hash": get_git_hash()
    })

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=int(os.getenv("PORT", 8000)))
    args = parser.parse_args()
    uvicorn.run("app.main:app", host="0.0.0.0", port=args.port)

