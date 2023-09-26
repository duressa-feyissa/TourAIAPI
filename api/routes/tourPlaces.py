from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from api.crud.tourPlace import get_tour_places, get_tour_place_by_id, create_tour_place, update_tour_place, delete_tour_place, get_tour_places_by_user_id
from api.helper.get_db import get_db
from api.schema import TourPlaceCreate

router = APIRouter()

@router.get("/tour_places")
async def read_tour_places(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await get_tour_places(db, skip=skip, limit=limit)

@router.get("/tour_places/{tour_place_id}")
async def read_tour_place(tour_place_id: str, db: Session = Depends(get_db)):
    tour_place = await get_tour_place_by_id(db, tour_place_id)
    if tour_place is None:
        raise HTTPException(status_code=404, detail="TourPlace not found")
    return tour_place

@router.get("/tour_places")
async def read_tour_places_by_user_id(user_id: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await get_tour_places()

@router.post("/tour_places")
async def create_tour_places(tour_place: TourPlaceCreate, db: Session = Depends(get_db)):
    result = await create_tour_place(db, tour_place)
    if result is None:
        raise HTTPException(status_code=400, detail="TourPlace not created")
    return result

@router.put("/tour_places/{tour_place_id}")
async def update_tour_places(tour_place_id: str, tour_place: dict, db: Session = Depends(get_db)):
    updated_tour_place = await update_tour_place(db, tour_place_id, tour_place)
    if updated_tour_place is None:
        raise HTTPException(status_code=404, detail="TourPlace not found")
    return updated_tour_place

@router.delete("/tour_places/{tour_place_id}")
async def delete_tour_places(tour_place_id: str, db: Session = Depends(get_db)):
    deleted_tour_place = await delete_tour_place(db, tour_place_id)
    if deleted_tour_place is None:
        raise HTTPException(status_code=404, detail="TourPlace not found")
    return deleted_tour_place

