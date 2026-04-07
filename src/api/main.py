from fastapi import FastAPI
from src.api.routers import router as user_router

def create_app() -> FastAPI:
    app = FastAPI(title="DDD Prototyping API", version="0.1.0")
    app.include_router(user_router)
    return app

app = create_app()