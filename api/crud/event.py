from uuid import uuid4
from sqlalchemy.orm import Session
from api.models import Event

async def get_events(db: Session, skip: int = 0, limit: int = 100, user_id: str = None):
    return db.query(Event).filter(Event.user_id == user_id).offset(skip).limit(limit).all()

async def get_event_by_id(db: Session, event_id: str):
    return db.query(Event).filter(Event.id == event_id).first() 

async def create_event(db: Session, event_data: dict, user_id: str):
    event_id = str(uuid4())
    db_event = Event(
        id=event_id,
        user_id=user_id,
        title=event_data.title,
        description=event_data.description,
        location=event_data.location,
        date=event_data.date,
        category=event_data.category,
        organizer=event_data.organizer,
        contact=event_data.contact,
        website=event_data.website,
        highlights=event_data.highlights,
        images=event_data.images,
        tickets=event_data.tickets
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

async def update_event(db: Session, event_id: str, event_data: dict, user_id: str):
    db_event = db.query(Event).filter(Event.user_id == user_id, Event.id == event_id).first()
    if db_event:
        for key, value in event_data.items():
            setattr(db_event, key, value)
        db.commit()
        db.refresh(db_event)
        return db_event
    return None

async def delete_event(db: Session, event_id: str, user_id: str):
    db_event = db.query(Event).filter(Event.user_id == user_id, Event.id == event_id).first()
    if db_event:
        db.delete(db_event)
        db.commit()
        return db_event
    return None
