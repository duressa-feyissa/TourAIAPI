from fastapi import APIRouter
from api.schema.event import Event, EventUpdate
from typing import List, Optional
from bson import ObjectId
from api.helper.db import db as db_client

user_id = "X"

router = APIRouter()
async def create_event(event: Event) -> Event:
    event_dict = event.dict()
    event_dict['user_id'] = user_id
    result = await db_client['events'].insert_one(event_dict)
    event.id = str(result.inserted_id)
    return event

async def get_all_events():
    events = []
    async for event in db_client['events'].find():
        event['_id'] = str(event['_id'])
        events.append(event)
    return events

async def get_event_by_id(event_id: str) -> Optional[Event]:
    event = await db_client['events'].find_one({"_id": ObjectId(event_id)})
    if event:
        return Event(**event)
    return None

async def update_event(event_id: str, updated_event_data: EventUpdate) -> Optional[Event]:
    updated_event = await db_client['events'].find_one_and_update(
        {"_id": ObjectId(event_id)},
        {"$set": updated_event_data.dict()},
        return_document=True
    )
    if updated_event:
        return Event(**updated_event)
    return None

async def delete_event(event_id: str) -> Optional[Event]:
    event = await db_client['events'].find_one({"_id": ObjectId(event_id)})
    result = await db_client['events'].delete_one({"_id": ObjectId(event_id)})
    if result.deleted_count == 1:
        return Event(**event)
    return None