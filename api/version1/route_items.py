from typing import List
from fastapi import Depends,APIRouter
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from api.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.repository.location import get_location_by_id
from db.session import get_db
from db.repository.items import create_new_item
from schemas.items import CreateItem, ShowItem

router = APIRouter()

@router.post("/", response_model=ShowItem)
async def create_item(location_id, item: CreateItem, db: Session = Depends(get_db), current_user:User = Depends(get_current_user_from_token)):
    location = get_location_by_id(location_id, db, current_user)

    if not location:
        raise HTTPException(status_code=404, detail="Location not found")

    new_item = create_new_item(location_id, item, db, current_user)
    return new_item

