from fastapi import FastAPI, Depends
from typing import List, Optional
from pydantic import BaseModel
from db.models.users import User
from db.session import engine
from db.base_class import Base
from db.base import Base
from api.version1 import route_users
from api.version1 import route_login 

from core.config import settings

from api.version1.route_login import get_current_user_from_token 

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    return app

def create_tables():
    Base.metadata.create_all(bind=engine)

app = start_application()

class Location(BaseModel):
    id: int
    name: str
    path: str
    user_id: int

locations: List[Location] = [Location(**{
  "id": 0,
  "name": "string",
  "path": "string",
  "user_id": 0
})]

current_id = 1

app.include_router(route_users.router, prefix="/users", tags=["users"])
app.include_router(route_login.router, prefix="/login", tags=["login"])

@app.get("/")
async def root(current_user:User = Depends(get_current_user_from_token)):
    return {"message": f"Hello World {current_user.username}!"}

@app.get("/locations", response_model=List[Location])
async def get_locations():
    return locations

@app.post("/locations", response_model=Location)
async def create_location(location: Location):
    global current_id 

    location.id = current_id
    current_id = current_id + 1

    locations.append(location)

    return location

@app.put("/locations/{location_id}")
async def update_locations(location_id: int, location: Location):
    print(locations)
    existing_location = next((location for location in locations if location.id == location_id), None)
    print(existing_location)

    if existing_location:
        existing_location.dict().update(location.dict())
        print(locations)
        return existing_location
    else:
        return {"error": f"Location with id {location_id} not found."}, 404

    

@app.get("/locations/{id}")
async def get_location(id: int):
    return {"data": {"name": f"Location {id}", "id": id}}

