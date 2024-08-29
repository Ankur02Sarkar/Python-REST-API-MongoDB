# models.py
from pydantic import BaseModel, Field
from typing import Optional

class UserModel(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: str
    email: str
    age: int

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "johndoe@example.com",
                "age": 30
            }
        }

class UpdateUserModel(BaseModel):
    name: Optional[str]
    email: Optional[str]
    age: Optional[int]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "age": 25
            }
        }
