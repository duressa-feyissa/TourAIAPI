from uuid import uuid4
from sqlalchemy.orm import Session
from api.models import User
from api.helper.security import get_password_hash
from api.schema import UserCreate

async def get_user_by_email(db: Session, email: str):
    result = await db.query(User).filter(User.email == email).first()
    if not result:
        return None
    return result.toJson()
        
async def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

async def get_user_by_id(db: Session, user_id: str):
    result = db.query(User).filter(User.id == user_id).first() 
    if result is None:
        return None
    return result.toJson()

async def create_user(db: Session, user_data: UserCreate):
    user_id = str(uuid4())
    if get_user_by_email(db, user_data.email) is None:
        return None
    db_user = User(id=user_id, firstname=user_data.firstname, lastname=user_data.lastname, email =user_data.email, password=get_password_hash(user_data.password), role=user_data.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user.toJson()

async def update_user(db: Session, user_id: str, user_data: dict):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        for key, value in user_data.items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user.toJson()
    return None

async def delete_user(db: Session, user_id: str):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user.toJson()
    return None
