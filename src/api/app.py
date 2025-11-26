from fastapi import FastAPI
from src.api.main import router
from src.database import database_run
from config.path import DATABASE
import os

def create_app() -> FastAPI:
    app = FastAPI()

    @app.on_event("startup")
    def startup_event():
        db_file = DATABASE / "database.db"
        if not os.path.exists(db_file):
            database_run()

    app.include_router(router)
    return app
