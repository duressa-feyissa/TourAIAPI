from pydantic import BaseModel

class Recommondation(BaseModel):
    chat: str
    
    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True


