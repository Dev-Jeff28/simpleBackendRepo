from fastapi import FastAPI

from .database import Base
from .database import engine

from .routers.students import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Student Management API Running"
    }