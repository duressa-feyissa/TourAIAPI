from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from api.helper.auth import create_access_token, verify_password, authenticate_user_by_token
from api.crud.user import get_user_by_email

router = APIRouter()
ACCESS_TOKEN_EXPIRE_MINUTES = 10000

@router.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    email = form_data.username
    password = form_data.password
    user = await get_user_by_email(email)

    if user is None or not verify_password(password, user.get('password')):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": email}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/current_user")
async def get_current_user(request: Request):
    token = request.query_params.get("token")

    if token is None:
        raise HTTPException(status_code=400, detail="Token not provided")
    user = authenticate_user_by_token(token)
    return user
