from fastapi import APIRouter, HTTPException
from api.schema.tourPlace import TourPlaceModel, TourPlace
from api.crud.tourPlace import (
    create_tour_place,
    get_tour_places,
    get_tour_place,
    update_tour_place,
    delete_tour_place,
)

router = APIRouter()

@router.post("/", response_model=TourPlace)
async def create_tour_place_route(tour_place: TourPlaceModel) -> TourPlace:
    return await create_tour_place(tour_place)

@router.get("/", response_model=list[TourPlace])
async def get_tour_places_route() -> list[TourPlace]:
    return await get_tour_places()

@router.get("/{id}/", response_model=TourPlace)
async def get_tour_place_route(id: str) -> TourPlace:
    tour_place = await get_tour_place(id)
    if tour_place is None:
        raise HTTPException(status_code=404, detail="Tour place not found")
    return tour_place

@router.put("/{id}/", response_model=TourPlace)
async def update_tour_place_route(id: str, tour_place_data: TourPlaceModel) -> TourPlace:
    tour_place = await update_tour_place(id, tour_place_data)
    if tour_place is None:
        raise HTTPException(status_code=404, detail="Tour place not found")
    return tour_place

@router.delete("/{id}/", response_model=TourPlace)
async def delete_tour_place_route(id: str) -> TourPlace:
    tour_place = await delete_tour_place(id)
    if tour_place is None:
        raise HTTPException(status_code=404, detail="Tour place not found")
    return tour_place
