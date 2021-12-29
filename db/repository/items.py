from sqlalchemy.orm import Session
from db.models.items import Item
from db.models.users import User
from schemas.items import CreateItem

def create_new_item(item: CreateItem, db: Session, current_user: User):
    new_item = Item(name=item.name, location_id=item.location_id, owner=current_user)

    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    print(new_item)
    return new_item

def get_items_by_location_id(location_id: int, db: Session, current_user: User):
    items = db.query(Item).filter(Item.location_id == location_id)
    return items