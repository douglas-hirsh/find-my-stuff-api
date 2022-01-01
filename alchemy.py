from sqlalchemy.orm import Session
from db.models.locations import Location
from db.models.items import Item

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings
from db.base import Base

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo="debug")

SessionLocal = sessionmaker(autocommit= False, autoflush= False,bind=engine)

Base.metadata.create_all(bind=engine)

db:Session = SessionLocal()

all_locations = db.query(Location).all()
print(all_locations)
for location in all_locations:
    location.items.append(Item(name="New Item", owner=location.owner))
    db.add(location)
    db.commit()

print(all_locations)