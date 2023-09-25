from typing import List
from fastapi import APIRouter, HTTPException
from api.schema.tourPlace import Accommodation, AccommodationModel
from api.crud.accomadation import create_accommodation, get_accommodations_for_tour_place, get_accommodation, update_accommodation, delete_accommodation

router = APIRouter()

@router.post("/tourplaces/{tour_place_id}/accommodations/", response_model=Accommodation)
async def create_accommodation_for_tour_place(tour_place_id: str, accommodation: AccommodationModel):
    return await create_accommodation(tour_place_id, accommodation)

@router.get("/tourplaces/{tour_place_id}/accommodations/", response_model=List[Accommodation])
async def read_accommodations_for_tour_place(tour_place_id: str):
    return await get_accommodations_for_tour_place(tour_place_id)

@router.get("/tourplaces/{tour_place_id}/accommodations/{accommodation_id}", response_model=Accommodation)
async def read_accommodation(tour_place_id: str, accommodation_id: str):
    accommodation = await get_accommodation(tour_place_id, accommodation_id)
    if accommodation is None:
        raise HTTPException(status_code=404, detail="Accommodation not found")
    return accommodation

@router.put("/tourplaces/{tour_place_id}/accommodations/{accommodation_id}", response_model=Accommodation)
async def update_accommodation_for_tour_place(tour_place_id: str, accommodation_id: str, accommodation_data: Accommodation):
    accommodation = await update_accommodation(tour_place_id, accommodation_id, accommodation_data)
    if accommodation is None:
        raise HTTPException(status_code=404, detail="Accommodation not found")
    return accommodation

@router.delete("/tourplaces/{tour_place_id}/accommodations/{accommodation_id}", response_model=Accommodation)
async def delete_accommodation_for_tour_place(tour_place_id: str, accommodation_id: str):
    accommodation = await delete_accommodation(tour_place_id, accommodation_id)
    if accommodation is None:
        raise HTTPException(status_code=404, detail="Accommodation not found")
    return accommodation

