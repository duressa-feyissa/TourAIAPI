from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field, validator
from api.model.pyObjectId import PyObjectId
from api.schema.user.example import example
from typing import Optional

class UserBase(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    firstname: str
    lastname: str
    email: EmailStr
    role: str
    profile_image: Optional[str]
    
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    def __get_pydantic_json_schema__(self, *, schema):
        return example

    @validator('role')
    def validate_role(cls, value):
        allowed_roles = ['admin', 'user', 'serviceProvider']
        if value.lower() not in allowed_roles:
            raise ValueError(f"Invalid role. Allowed roles are {', '.join(allowed_roles)}")
        return value

class User(UserBase):
    pass

class UserModel(UserBase):
    password: str

class UserUpdateModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    role: Optional[str]
    profile_image: Optional[str]
    password: Optional[str]
    
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    def __get_pydantic_json_schema__(self, *, schema):
        return example 

    @validator('role')
    def validate_role(cls, value):
        allowed_roles = ['admin', 'user', 'serviceProvider']
        if value and value.lower() not in allowed_roles:
            raise ValueError(f"Invalid role. Allowed roles are {', '.join(allowed_roles)}")
        return value
