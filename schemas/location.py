from pydantic import BaseModel, EmailStr

from schemas.users import ShowUser

class LocationBase(BaseModel):
    name: str

class CreateLocation(LocationBase):
    pass

class ShowLocation(LocationBase):
    owner: ShowUser

    class Config():
        orm_mode = True