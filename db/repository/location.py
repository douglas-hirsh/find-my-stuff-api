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

def get_all_locations(db: Session, current_user: User):
    locations = db.query(Location).filter(Location.owner_id == current_user.id).all()
    return locations

def get_location_by_id(id: int, db: Session, current_user: User):
    location = db.query(Location).filter(Location.owner_id == current_user.id).filter(Location.id == id).first()
    return location