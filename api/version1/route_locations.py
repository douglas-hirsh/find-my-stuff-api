from typing import List
from fastapi import Depends,APIRouter
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from api.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.repository.location import create_new_location, get_all_locations, get_location_by_id, update_location
from db.session import get_db

from schemas.location import CreateLocation, ShowLocation

router = APIRouter()

@router.get("/", response_model=List[ShowLocation])
async def get_locations(db: Session = Depends(get_db), current_user:User = Depends(get_current_user_from_token)):
    print('hello')
    locations = get_all_locations(db, current_user)
    print(locations)
    return locations

@router.post("/", response_model=ShowLocation)
async def create_location(location: CreateLocation, db: Session = Depends(get_db), current_user:User = Depends(get_current_user_from_token)):
    location = create_new_location(location, db, current_user)
    return location

@router.put("/{id}", response_model=ShowLocation)
async def update_locations(id: int, location: CreateLocation, db: Session = Depends(get_db), current_user:User = Depends(get_current_user_from_token)):
    existing_location = get_location_by_id(id, db, current_user)

    if not existing_location:
        raise HTTPException(status_code=404, detail="Location not found")

    update_location(existing_location, location, db, current_user)

    return existing_location

    

@router.get("/{id}", response_model=ShowLocation)
async def get_location(id: int, db: Session = Depends(get_db), current_user:User = Depends(get_current_user_from_token)):
    location = get_location_by_id(id, db, current_user)

    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    return location
