from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.helper.get_db import get_db
from api.helper.chat.recommandation import recommandation
from api.schema import Recommendation
router = APIRouter()

@router.post("/recommendation")
async def make_recommendation(chat: Recommendation, db: Session = Depends(get_db)):
    result =  await recommandation(chat.chat, db)
    if result is None:
        raise HTTPException(status_code=404, detail="Recommendation failed")
    return result


