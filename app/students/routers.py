from fastapi import APIRouter, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson import ObjectId

from .models import StudentModel, UpdateStudentModel
from .services import (
    add_student, retrieve_filtered_student,
    retrieve_student, update_student, delete_student
)

router = APIRouter()


@router.post("/")
async def api_create_student(student: StudentModel = Body(...)):
    """
    Add a new student.
    """
    student = jsonable_encoder(student)
    new_student = await add_student(student)

    return JSONResponse(status_code=status.HTTP_201_CREATED,
                        content={"id": str(new_student.inserted_id)})


@ router.get("/")
async def api_filter_students(country: str | None = None,
                              age: int | None = None):
    """
    List all students with optional country and age filters.
    """
    students = await retrieve_filtered_student(country, age)
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": students})


@ router.get("/{id}")
async def api_get_student(id: str):
    """
    Get details of a single student by ID.
    """
    if (student := await retrieve_student(id)) is not None:
        return JSONResponse(status_code=status.HTTP_200_OK,
                            content=student)

    raise HTTPException(status_code=404, detail="Student not found")


@ router.patch("/{id}")
async def api_update_student(
        id: str,
        student: UpdateStudentModel = Body(...)):
    """
    Update details of a single student by ID.
    """

    student = {k: v for k, v in student.model_dump(
        exclude_unset=True).items() if v is not None}

    is_updated = await update_student(id, student)

    if is_updated:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT,
                            content={})

    raise HTTPException(status_code=404, detail="Error occurred")


@ router.delete("/{id}")
async def api_delete_student(id: str):
    """
    Delete a student by ID.
    """
    is_deleted = await delete_student(id)

    if is_deleted:
        return JSONResponse(status_code=status.HTTP_200_OK, content={})

    raise HTTPException(status_code=404, detail="Student not found")
