from typing import List
from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from api.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.repository.location import create_new_location, get_all_locations
from db.session import get_db

from schemas.location import CreateLocation, ShowLocation

router = APIRouter()

@router.get("/", response_model=List[ShowLocation])
async def get_locations(db: Session = Depends(get_db), current_user:User = Depends(get_current_user_from_token)):
    print('hello')
    locations = get_all_locations(db, User(id=1))
    print(locations)
    return locations

@router.post("/", response_model=ShowLocation)
async def create_location(location: CreateLocation, db: Session = Depends(get_db), current_user:User = Depends(get_current_user_from_token)):
    location = create_new_location(location, db, current_user)
    return location

@router.put("/{location_id}")
async def update_locations(location_id: int, location: CreateLocation):

    existing_location = None
    print(existing_location)

    if existing_location:
        existing_location.dict().update(location.dict())

        return existing_location
    else:
        return {"error": f"Location with id {location_id} not found."}, 404

    

@router.get("/{id}")
async def get_location(id: int):
    return {"data": {"name": f"Location {id}", "id": id}}