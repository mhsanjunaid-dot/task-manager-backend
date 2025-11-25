from fastapi import FastAPI
from . import models
from .database import engine
from .routers import tasks

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tasks.router)

@app.get("/")
def home():
    return {"message": "Backend is running!"}
