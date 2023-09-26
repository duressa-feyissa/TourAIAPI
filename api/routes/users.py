from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.crud.user import get_users, get_user_by_id, create_user, update_user, delete_user
from api.helper.get_db import get_db
from api.schema import UserCreate

router = APIRouter()

@router.get("/users")
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await get_users(db, skip=skip, limit=limit)

@router.get("/users/{user_id}")
async def read_user(user_id: str, db: Session = Depends(get_db)):
    user = await get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users")
async def create_users(user: UserCreate, db: Session = Depends(get_db)):
    result = await create_user(db, user)
    if result is None:
        raise HTTPException(status_code=400, detail="User not created")
    return result

@router.put("/users/{user_id}")
async def update_users(user_id: str, user: dict, db: Session = Depends(get_db)):
    updated_user = await update_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/{user_id}")
async def delete_users(user_id: str, db: Session = Depends(get_db)):
    deleted_user = await delete_user(db, user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user

