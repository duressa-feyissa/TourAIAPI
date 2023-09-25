from typing import List, Optional

from bson import ObjectId
from api.model.pyObjectId import PyObjectId
from api.schema.event.example import example
from pydantic import BaseModel, Field

class TicketInfo(BaseModel):
    available: Optional[str]
    price: Optional[str]

class ImageDetails(BaseModel):
    url: Optional[str]
    caption: Optional[str]

class Event(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: Optional[str]
    title: str
    description: str
    location: str
    date: str
    category: List[str]
    organizer: str
    contact: str
    website: Optional[str]
    tickets: TicketInfo
    highlights: List[str]
    images: List[ImageDetails]

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    def __get_pydantic_json_schema__(self, *, schema):
        return example

    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls, values):
        return values

    def __get_pydantic_json_schema__(self, *, schema):
        return example

class EventUpdate(BaseModel):
    title: Optional[str]
    user_id: Optional[str]
    description: Optional[str]
    location: Optional[str]
    date: Optional[str]
    category: Optional[List[str]]
    organizer: Optional[str]
    contact: Optional[str]
    website: Optional[str]
    tickets: Optional[TicketInfo]
    highlights: Optional[List[str]]
    images: Optional[List[ImageDetails]]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        
    def __get_pydantic_json_schema__(self, *, schema):
        return example
