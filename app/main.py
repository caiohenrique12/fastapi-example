from fastapi import FastAPI

from .routers import customers

app = FastAPI(title="FastAPI, Docker, and Traefik")

app.include_router(customers.router)


@app.get("/")
async def read_root():
    return {"hello": "world"}