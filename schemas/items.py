from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str

class CreateItem(ItemBase):
    location_id: int

class ShowItem(ItemBase):
    id: int
    class Config():
        orm_mode = True