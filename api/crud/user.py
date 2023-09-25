from bson import ObjectId
from typing import List, Optional
from api.schema.user import UserModel, UserUpdateModel
from api.helper.db import db
from api.helper.security import get_password_hash

async def email_exists(email: str) -> bool:
    existing_user = await db['users'].find_one({"email": email})
    return existing_user is not None

async def create_user(user: UserModel) -> Optional[UserModel]:
    user_dict = user.dict()
    user_dict['password'] = get_password_hash(user_dict['password'])
    result = await db['users'].insert_one(user_dict)
    user.id = str(result.inserted_id)
    return user

async def get_all_users() -> List[UserModel]:
    users = []
    async for user in db['users'].find():
        users.append(UserModel(**user))
    return users

async def get_user_by_id(user_id: str) -> Optional[UserModel]:
    user = await db['users'].find_one({"_id": ObjectId(user_id)})

    if user:
        return UserModel(**user)
    return None

async def update_user(user_id: str, updated_user_data: UserUpdateModel) -> Optional[UserModel]:
    updated_user = await db['users'].find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$set": updated_user_data.dict()},
        return_document=True
    )
    if updated_user:
        return UserModel(**updated_user)
    return None

async def delete_user(user_id: str) -> Optional[UserModel]:
    user = await get_user_by_id(user_id)
    await db['users'].delete_one({"_id": ObjectId(user_id)})
    if user:
        return UserModel(**user)
    return None

async def get_user_email(email: str):
    user = await db['users'].find_one({"email": email})
    if user:
        return user
    return None