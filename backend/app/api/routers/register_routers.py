from fastapi import FastAPI
from .home import home
from .search import search

def register_routers(app: FastAPI) -> None:
    app.include_router(home)
    app.include_router(search)