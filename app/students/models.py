from typing import Optional
from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str = Field(...)
    country: str = Field(...)


class StudentModel(BaseModel):
    name: str = Field(...)
    age: int = Field(..., ge=0, )
    address: Address = Field(...)


class UpdateAddress(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None


class UpdateStudentModel(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[UpdateAddress] = None
