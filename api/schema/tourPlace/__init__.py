from pydantic import BaseModel, Field
from bson import ObjectId
from typing import List, Optional
from api.model.pyObjectId import PyObjectId
from api.schema.tourPlace.example import example

class WeatherModel(BaseModel):
    description: str
    averageTemp: float

class ActivityModel(BaseModel):
    name: str
    description: str

class LocationModel(BaseModel):
    latitude: str
    longitude: str
    address: str

class ImageModel(BaseModel):
    url: str
    caption: str
    
class Accommodation(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: Optional[str]
    name: str
    type: List[str]
    description: str
    location: LocationModel
    contact: str
    website: str
    images: List[ImageModel]
    service: List[str]
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = example

class AccommodationModel(Accommodation):
    pass

class AccommodationModelUpdate(BaseModel):
    name: Optional[str]
    type: Optional[List[str]]
    description: Optional[str]
    location: Optional[LocationModel]
    contact: Optional[str]
    website: Optional[str]
    images: Optional[List[ImageModel]]
    service: Optional[List[str]]

class TourPlace(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    description: List[str]
    location: LocationModel
    category: List[str]
    highlights: List[str]
    images: List[ImageModel]
    activities: List[ActivityModel]
    Weather: WeatherModel
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = example
        
class TourPlaceModel(TourPlace):
        Accommodation: Optional[List[AccommodationModel]]
    
        
class TourPlaceUpdateModel(BaseModel):
    name: Optional[str]
    description: Optional[List[str]]
    location: Optional[LocationModel]
    category: Optional[List[str]]
    highlights: Optional[List[str]]
    images: Optional[List[ImageModel]]
    activities: Optional[List[ActivityModel]]
    Weather: Optional[WeatherModel]
    Accommodation: Optional[List[AccommodationModel]]
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
