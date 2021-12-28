from sqlalchemy.orm import Session
from db.models.locations import Location
from schemas.location import CreateLocation

from schemas.users import UserCreate
from db.models.users import User
from core.hashing import Hasher

def create_new_location(location: CreateLocation, db: Session, current_user: User):
    location = Location(name=location.name, owner=current_user)
    
    db.add(location)
    db.commit()
    db.refresh(location)
    return location    