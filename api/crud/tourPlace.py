from bson import ObjectId
from typing import List, Optional
from api.schema.tourPlace import TourPlaceModel, TourPlaceUpdateModel
from api.helper.db import db

async def create_tour_place(tour_place: TourPlaceModel) -> Optional[TourPlaceModel]:
    tour_place_dict = tour_place.dict()
    result = await db['TourPlace'].insert_one(tour_place_dict)
    tour_place.id = result.inserted_id
    return tour_place

async def get_tour_places() -> List[TourPlaceModel]:
    tour_places = []
    async for tour_place in db['TourPlace'].find():
        tour_places.append(tour_place)
    return tour_places

async def get_tour_place(id: str) -> Optional[TourPlaceModel]:
    tour_place = await db['TourPlace'].find_one({"_id": ObjectId(id)})
    return tour_place

async def update_tour_place(id: str, tour_place_data: TourPlaceModel) -> Optional[TourPlaceModel]:
    updated_tour_place = await db['TourPlace'].find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": tour_place_data.dict()},
        return_document=True
    )
    if updated_tour_place:
        return updated_tour_place
    return None
        

async def delete_tour_place(id: str) -> Optional[TourPlaceModel]:
    tour_place = await get_tour_place(id)
    result = await db['TourPlace'].delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return tour_place
    return None