#!/usr/bin/python3
"""Amenity file"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from sqlalchemy import Column, String, ForeignKey


class Amenity(BaseModel, Base):
    """Amenity Class"""

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    # Define the primary key for the amenities table
    id = Column(String(60), primary_key=True, nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity")
