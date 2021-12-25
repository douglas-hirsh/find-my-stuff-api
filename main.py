from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from db.session import engine
from db.base_class import Base

from core.config import settings

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

@app.get("/")
async def root():
    return {"message": "Hello World"}

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

