from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.helper.get_db import get_db  
from api.crud.accomadation import get_accommodation_by_id, get_accommodations, create_accommodation, update_accommodation, delete_accommodation
from api.schema import Accommodation, AccommodationCreate

router = APIRouter()

@router.get("/tour_places/{tour_place_id}/accommodations")
async def read_accommodations(tour_place_id: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await get_accommodations(db, skip=skip, limit=limit, tour_place_id=tour_place_id)

@router.get("/accommodations/{accommodation_id}")
async def read_accommodation(accommodation_id: str, db: Session = Depends(get_db)):
    accommodation = await get_accommodation_by_id(db, accommodation_id)
    if accommodation is None:
        raise HTTPException(status_code=404, detail="Accommodation not found")
    return accommodation

@router.post("/tour_places/{tour_place_id}/accommodations")
async def create_accommodations( tour_place_id: str, accommodation: AccommodationCreate, db: Session = Depends(get_db)):
    result = await create_accommodation(db, accommodation, tour_place_id)
    if result is None:
        raise HTTPException(status_code=400, detail="Accommodation not created")
    return result

@router.put("/accommodations/{accommodation_id}")
async def update_accommodations(accommodation_id: str, accommodation: AccommodationCreate, db: Session = Depends(get_db)):
    updated_accommodation = await update_accommodation(db, accommodation_id, accommodation.dict())
    if updated_accommodation is None:
        raise HTTPException(status_code=404, detail="Accommodation not found")
    return updated_accommodation

@router.delete("/accommodations/{accommodation_id}")
async def delete_accommodations(accommodation_id: str, db: Session = Depends(get_db)):
    deleted_accommodation = await delete_accommodation(db, accommodation_id)
    if deleted_accommodation is None:
        raise HTTPException(status_code=404, detail="Accommodation not found")
    return deleted_accommodation
