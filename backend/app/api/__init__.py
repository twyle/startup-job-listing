from fastapi import FastAPI
from .routers import register_routers

def create_app():
    app = FastAPI()
    register_routers(app)
    
    return app