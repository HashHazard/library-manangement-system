from bson import ObjectId
from ..database import db_collection


async def add_student(student_data: dict):
    """
    Add a new student to the database
    """
    return await db_collection.insert_one(student_data)


async def retrieve_filtered_student(country: str | None = None, age: int | None = None):
    """
    Return a list of students with optional country and age filter
    """
    students = []
    if country and age:
        async for student in db_collection.find({"address.country": country, "age": {"$gte": age}}):
            students.append({"name": student["name"], "age": student["age"]})
    elif country:
        async for student in db_collection.find({"address.country": country}):
            students.append({"name": student["name"], "age": student["age"]})
    elif age:
        async for student in db_collection.find({"age": {"$gte": age}}):
            students.append({"name": student["name"], "age": student["age"]})
    else:
        async for student in db_collection.find({}):
            students.append({"name": student["name"], "age": student["age"]})

    return students


async def retrieve_student(id: str):
    """
    Return details of a single student
    """
    if ObjectId.is_valid(id):
        student = await db_collection.find_one({"_id": ObjectId(id)}, {"_id": 0})
        return student
    return None


async def update_student(id: str, data: dict):
    """
    Update student data and return confirmation
    """
    student = await retrieve_student(id)
    if student:
        if len(data) < 1:
            return False

        result = await db_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return result.modified_count > 0
    return False


async def delete_student(id: str):
    """
    Delete student data
    """
    student = await retrieve_student(id)
    if student:
        delete_result = await db_collection.delete_one({"_id": ObjectId(id)})
        if delete_result.deleted_count == 1:
            return True
    return False
