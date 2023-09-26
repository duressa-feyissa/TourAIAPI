from pydantic import BaseModel, Field
from typing import List, Optional

class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: str
    role: str
    
    class Config:
        arbitrary_types_allowed=True


class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str


class AccommodationBase(BaseModel):
    name: str
    type: List[str]
    user_id: str
    description: str
    location: dict
    contact: str
    website: Optional[str]
    images: List[dict]
    service: List[str]

    
    class Config:
        arbitrary_types_allowed=True


class AccommodationCreate(AccommodationBase):
    pass

class Accommodation(AccommodationBase):
    id: str
    user_id: Optional[str]
    tour_place_id: Optional[str]

    
    class Config:
        arbitrary_types_allowed=True


class TourPlaceBase(BaseModel):
    name: str
    description: List[str]
    location: dict
    category: List[str]
    highlights: List[str]
    images: List[dict]
    activities: List[dict]
    weather: dict

    
    class Config:
        arbitrary_types_allowed=True

class TourPlaceCreate(TourPlaceBase):
    pass

class TourPlace(TourPlaceBase):
    id: str

class EventBase(BaseModel):
    title: str
    description: str
    location: str
    date: str
    category: List[str]
    organizer: str
    contact: str
    website: Optional[str]
    highlights: List[str]
    images: List[dict]
    tickets: dict

    
    class Config:
        arbitrary_types_allowed=True


class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: str
    user_id: Optional[str]



class Recommendation(BaseModel):
    chat: str
    
    
    class Config:
        arbitrary_types_allowed=True
