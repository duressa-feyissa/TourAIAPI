from fastapi import APIRouter, HTTPException
from typing import List

from fastapi.params import Depends
from api.helper.protected import check_user_role
from api.schema.user import  UserModel, UserUpdateModel, User
from api.crud.user import (
    email_exists,
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user,
)

router = APIRouter()

@router.post("/", response_model=User)
async def create_user_route(user: UserModel) -> User:
    user_exists = await email_exists(user.email)
    if user_exists:
        raise HTTPException(status_code=400, detail="Email already exists")
    created_user = await create_user(user)
    if created_user:
        return created_user
    raise HTTPException(status_code=500, detail="Could not create user")

@router.get("/", response_model=List[User])
async def get_all_users_route() -> List[User]:
    return await get_all_users()

@router.get("/{user_id}/", response_model=User)
async def get_user_by_id_route(user_id: str) -> User:
    user = await get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{user_id}/", response_model=User)
async def update_user_route(user_id: str, updated_user_data: UserUpdateModel) -> User:
    updated_user = await update_user(user_id, updated_user_data)
    if updated_user:
        return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}/", response_model=User)
async def delete_user_route(user_id: str) -> User:
    deleted_user = await delete_user(user_id)
    if deleted_user:
        return deleted_user
    raise HTTPException(status_code=404, detail="User not found")
