import uvicorn
from fastapi import FastAPI, Response

from app.students.routers import router as student_router
from config import settings

app = FastAPI()

app.include_router(student_router, tags=["students"], prefix="/students")


@app.get("/")
def read_root():
    return Response("Server is running.")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT
    )
