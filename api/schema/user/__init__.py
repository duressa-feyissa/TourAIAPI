from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field, validator
from api.model.pyObjectId import PyObjectId
from api.schema.user.example import example
from typing import Optional

class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    firstname: str
    lastname: str
    email: EmailStr
    role: str
    profile_image: Optional[str]
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = example

    @validator('role')
    def validate_role(cls, value):
        allowed_roles = ['admin', 'user', 'serviceProvider']
        if value not in allowed_roles:
            raise ValueError(f"Invalid role. Allowed roles are {', '.join(allowed_roles)}")
        return value

class UserModel(User):
    password: str


class UserUpdateModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    role: Optional[str]
    profile_image: Optional[str]
    password: Optional[str]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = example

    @validator('role')
    def validate_role(cls, value):
        allowed_roles = ['admin', 'user', 'serviceProvider']
        if value and value not in allowed_roles:
            raise ValueError(f"Invalid role. Allowed roles are {', '.join(allowed_roles)}")
        return value
