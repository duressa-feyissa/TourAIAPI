from bson import ObjectId
from typing import List, Optional
from api.schema.tourPlace import Accommodation, AccommodationModel, AccommodationModelUpdate
from api.helper.db import db

user_id = "ds"
async def create_accommodation(tour_place_id: str, accommodation: AccommodationModel) -> Optional[Accommodation]:
    tour_place = await db['TourPlace'].find_one({"_id": ObjectId(tour_place_id)})
    if not tour_place:
        return None
    accommodation_dict = accommodation.dict()
    accommodation_id = str(ObjectId())
    accommodation_dict['_id'] = accommodation_id
    accommodation_dict['user_id'] = user_id
    tour_place.setdefault('accommodations', []).append(accommodation_dict)
    await db['TourPlace'].update_one({"_id": ObjectId(tour_place_id)}, {"$set": tour_place})
    return AccommodationModel(**accommodation_dict)

async def get_accommodations_for_tour_place(tour_place_id: str) -> List[Accommodation]:
    tour_place = await db['TourPlace'].find_one({"_id": ObjectId(tour_place_id)})
    if not tour_place or 'accommodations' not in tour_place:
        return []
    accommodations = tour_place['accommodations']
    result = []
    for accoummodation in accommodations:
        if accoummodation['user_id'] == user_id:
            result.append(AccommodationModel(**accoummodation))
    return result

async def get_accommodation(tour_place_id: str, accommodation_id: str) -> Optional[Accommodation]:
    tour_place = await db['TourPlace'].find_one({"_id": ObjectId(tour_place_id)})

    if not tour_place or 'accommodations' not in tour_place:
        return None
    accommodation = next((acc for acc in tour_place['accommodations'] if str(acc['_id']) == accommodation_id) , None)

    if accommodation:
        return AccommodationModel(**accommodation)

    return None

async def update_accommodation(tour_place_id: str, accommodation_id: str, accommodation_data: AccommodationModelUpdate) -> Optional[Accommodation]:
    tour_place = await db['TourPlace'].find_one({"_id": ObjectId(tour_place_id)})
    if not tour_place or 'accommodations' not in tour_place:
        return None
    for accommodation in tour_place['accommodations']:
        if str(accommodation['_id']) == accommodation_id:
            accommodation_data_dict = accommodation_data.dict(exclude_unset=True)
            accommodation.update(accommodation_data_dict)
            await db['TourPlace'].update_one({"_id": ObjectId(tour_place_id)}, {"$set": tour_place}) 
            return AccommodationModel(**accommodation)
    return None

async def delete_accommodation(tour_place_id: str, accommodation_id: str) -> Optional[Accommodation]:
    tour_place = await db['TourPlace'].find_one({"_id": ObjectId(tour_place_id)})

    if not tour_place or 'accommodations' not in tour_place:
        return None
    deleted = None
    updated_accommodations = []

    for acc in tour_place['accommodations']:
        if str(acc['_id']) != accommodation_id:
            updated_accommodations.append(acc)
        else:
            deleted = acc
    if len(updated_accommodations) < len(tour_place['accommodations']):
        await db['TourPlace'].update_one({"_id": ObjectId(tour_place_id)}, {"$set": {"accommodations": updated_accommodations}})
        return AccommodationModel(**deleted)
    return None

