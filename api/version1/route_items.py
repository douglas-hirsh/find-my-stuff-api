from typing import List
from fastapi import Depends,APIRouter
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from api.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.session import get_db
from db.repository.items import create_new_item
from schemas.items import CreateItem, ShowItem

router = APIRouter()

@router.post("/", response_model=ShowItem)
async def create_item(item: CreateItem, db: Session = Depends(get_db), current_user:User = Depends(get_current_user_from_token)):
    new_item = create_new_item(item, db, current_user)
    return new_item

