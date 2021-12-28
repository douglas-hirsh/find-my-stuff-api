from fastapi import FastAPI, Depends
from typing import List, Optional
from pydantic import BaseModel
from db.models.users import User
from db.repository.location import create_new_location
from db.session import engine, get_db
from db.base_class import Base
from db.base import Base
from api.version1 import route_users
from api.version1 import route_login 
from sqlalchemy.orm import Session

from core.config import settings

from api.version1.route_login import get_current_user_from_token
from schemas.location import CreateLocation, ShowLocation 

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    return app

def create_tables():
    Base.metadata.create_all(bind=engine)

app = start_application()

app.include_router(route_users.router, prefix="/users", tags=["users"])
app.include_router(route_login.router, prefix="/login", tags=["login"])

@app.get("/")
async def root(current_user:User = Depends(get_current_user_from_token)):
    return {"message": f"Hello World {current_user.username}!"}

@app.get("/locations", response_model=List[ShowLocation])
async def get_locations():
    return {"Locations": "Data"}

@app.post("/locations", response_model=ShowLocation)
async def create_location(location: CreateLocation, db: Session = Depends(get_db), current_user:User = Depends(get_current_user_from_token)):
    location = create_new_location(location, db, current_user)
    return location

@app.put("/locations/{location_id}")
async def update_locations(location_id: int, location: CreateLocation):

    existing_location = None
    print(existing_location)

    if existing_location:
        existing_location.dict().update(location.dict())

        return existing_location
    else:
        return {"error": f"Location with id {location_id} not found."}, 404

    

@app.get("/locations/{id}")
async def get_location(id: int):
    return {"data": {"name": f"Location {id}", "id": id}}

