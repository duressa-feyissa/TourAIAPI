from fastapi import APIRouter, HTTPException, Path
from typing import List
from api.schema.event import Event, EventUpdate
from api.crud.event import create_event, get_all_events, get_event_by_id, update_event, delete_event

router = APIRouter()

@router.post("/", response_model=Event)
async def create_events(event: Event) -> Event:
    return await create_event(event)

@router.get("/", response_model=List[Event])
async def get_all_Events() -> List[Event]:
    return await get_all_events()

@router.get("/{event_id}/", response_model=Event)
async def get_event(event_id: str = Path(..., title="Event ID")) -> Event:
    event = await get_event_by_id(event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.put("/{event_id}/", response_model=Event)
async def update_the_event(event_id: str, event_update: EventUpdate) ->Event:
    updated_event = await update_event(event_id, event_update)
    if updated_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event

@router.delete("/{event_id}/", response_model=Event)
async def delete_the_event(event_id: str) -> Event:
    deleted_event = await delete_event(event_id)
    if deleted_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return deleted_event
