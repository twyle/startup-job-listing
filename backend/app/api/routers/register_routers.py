from fastapi import FastAPI
from .home import home

def register_routers(app: FastAPI) -> None:
    app.include_router(home)