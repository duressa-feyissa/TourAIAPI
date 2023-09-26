from uuid import uuid4
from sqlalchemy.orm import Session
from api.models import Accommodation
from api.schema import AccommodationCreate

async def get_accommodations(db: Session, skip: int = 0, limit: int = 100, tour_place_id: str = None):
    return  db.query(Accommodation).filter(Accommodation.tour_place_id == tour_place_id).offset(skip).limit(limit).all()

async def get_accommodation_by_id(db: Session, accommodation_id: str):
    return db.query(Accommodation).filter(Accommodation.id == accommodation_id).first() 

async def create_accommodation(db: Session, accommodation_data: AccommodationCreate, tour_place_id: str):
    accommodation_id = str(uuid4())
    db_accommodation = Accommodation(
        id = accommodation_id,
        user_id = accommodation_data.user_id,
        tour_place_id = tour_place_id,
        name = accommodation_data.name,
        type = accommodation_data.type,
        description = accommodation_data.description,
        location = accommodation_data.location,
        contact = accommodation_data.contact,
        website = accommodation_data.website,
        images = accommodation_data.images,
        service = accommodation_data.service
    )
    db.add(db_accommodation)
    db.commit()
    db.refresh(db_accommodation)
    return db_accommodation

async def update_accommodation(db: Session, accommodation_id: str, accommodation_data: dict):
    db_accommodation = db.query(Accommodation).filter(Accommodation.id == accommodation_id).first()
    if db_accommodation:
        for key, value in accommodation_data.items():
            setattr(db_accommodation, key, value)
        db.commit()
        db.refresh(db_accommodation)
        return db_accommodation
    return None

async def delete_accommodation(db: Session, accommodation_id: str):
    db_accommodation = db.query(Accommodation).filter(Accommodation.id == accommodation_id).first()
    if db_accommodation:
        db.delete(db_accommodation)
        db.commit()
        return db_accommodation
    return None
