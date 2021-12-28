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
from api.version1 import route_locations 
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
app.include_router(route_locations.router, prefix="/locations", tags=["locations"])

@app.get("/")
async def root(current_user:User = Depends(get_current_user_from_token)):
    return {"message": f"Hello World {current_user.username}!"}

