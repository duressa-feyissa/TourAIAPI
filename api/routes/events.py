from fastapi import APIRouter, Depends, HTTPException, Path
from typing import List
from sqlalchemy.orm import Session
from api.crud.event import get_events, get_event_by_id, create_event, update_event, delete_event
from api.helper.get_db import get_db
from api.schema import EventCreate

router = APIRouter()

@router.get("/events/{event_id}")
async def read_event(event_id: str, db: Session = Depends(get_db)):
    event = await get_event_by_id(db, event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.get("/users/{user_id}/events")
async def read_events(user_id: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await get_events(db, skip=skip, limit=limit, user_id=user_id)



@router.post("/users/{user_id}/events")
async def create_events(user_id: str, event: EventCreate, db: Session = Depends(get_db)):
    result = await create_event(db, event, user_id)
    if result is None:
        raise HTTPException(status_code=400, detail="Event not created")
    return result

@router.put("/events/{event_id}")
async def update_events(event_id: str, event: dict, user_id: str, db: Session = Depends(get_db)):
    updated_event = await update_event(db, event_id, event, user_id)
    if updated_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event

@router.delete("/events/{event_id}")
async def delete_events(event_id: str, user_id: str, db: Session = Depends(get_db)):
    deleted_event = await delete_event(db, event_id, user_id)
    if deleted_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return deleted_event