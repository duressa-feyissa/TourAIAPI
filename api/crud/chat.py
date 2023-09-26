from api.helper.chat import recommandation
from api.schema import Recommondation

async def make_recommondation_for_place(chat: Recommondation):
    result =  await recommandation(chat.chat)
    if result['status'] == 'failed':
        return None
    return result
    