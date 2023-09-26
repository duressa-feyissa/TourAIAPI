from uuid import uuid4
from sqlalchemy.orm import Session
from api.models import TourPlace
from api.schema import TourPlaceCreate

async def get_tour_places(db: Session, skip: int = 0, limit: int = 100):
    return  db.query(TourPlace).all()

async def get_tour_place_by_id(db: Session, tour_place_id: str):
    return db.query(TourPlace).filter(TourPlace.id == tour_place_id).first() 

async def get_tour_places_by_user_id(db: Session, user_id: str):
    return db.query(TourPlace).filter(TourPlace.user_id == user_id)

async def create_tour_place(db: Session, tour_place_data: TourPlaceCreate):
    tour_place_id = str(uuid4())
    db_tour_place = TourPlace(
        id=tour_place_id,
        name = tour_place_data.name,
        description = tour_place_data.description,
        location = tour_place_data.location,
        category = tour_place_data.category ,
        highlights = tour_place_data.highlights ,
        images = tour_place_data.images,
        activities = tour_place_data.activities, 
        weather = tour_place_data.weather
    )
    db.add(db_tour_place)
    db.commit()
    db.refresh(db_tour_place)
    return db_tour_place

async def update_tour_place(db: Session, tour_place_id: str, tour_place_data: dict):
    db_tour_place = db.query(TourPlace).filter(TourPlace.id == tour_place_id).first()
    if db_tour_place:
        for key, value in tour_place_data.items():
            setattr(db_tour_place, key, value)
        db.commit()
        db.refresh(db_tour_place)
        return db_tour_place
    return None

async def delete_tour_place(db: Session, tour_place_id: str):
    db_tour_place = db.query(TourPlace).filter(TourPlace.id == tour_place_id).first()
    if db_tour_place:
        db.delete(db_tour_place)
        db.commit()
        return db_tour_place
    return None





