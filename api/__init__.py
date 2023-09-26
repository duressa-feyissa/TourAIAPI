import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.helper.protected import RoleBasedMiddleware
from api.routes.tourPlaces import router as tour_place_router
from api.routes.users import router as user_router
from api.routes.events import router as event_router
from api.routes.accomadations import router as accommodation_router
from api.routes.chats import router as chat_router
from api.helper.database import  engine
from api.models import Base

Base.metadata.create_all(bind=engine)

PORT = os.getenv("PORT", 8000)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],    
)
app.router.route_class = RoleBasedMiddleware
app.include_router(tour_place_router, prefix="/api/v1", tags=["tour_places"])
app.include_router(accommodation_router, prefix="/api/v1", tags=["accommodations"])
app.include_router(user_router, prefix="/api/v1", tags=["users"])
app.include_router(event_router, prefix="/api/v1", tags=["events"])
app.include_router(chat_router, prefix="/api/v1/chats", tags=["chats"])
