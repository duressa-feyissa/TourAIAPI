from fastapi import APIRouter, HTTPException
from typing import List
from api.schema.chat import Recommondation
from api.helper.chat.recommandation import recommandation
router = APIRouter()

@router.post("/recommendation")
async def make_recommendation(chat: Recommondation):
    result =  await recommandation(chat.chat)
    if result is None:
        raise HTTPException(status_code=404, detail="Recommendation failed")
    return result


