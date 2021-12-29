from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Item(Base):
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship("User", back_populates="items")
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship("Location", back_populates="items")