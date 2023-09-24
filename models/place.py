#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.amenity import Amenity
from models.review import Review

# Define the place_amenity Table first (to avoid circular import issues)
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )

class Place(BaseModel, Base):
    """A place to stay."""
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    # Define relationships with other classes
    reviews = relationship('Review', backref='place', cascade='delete')

    # Define the amenities relationship using the place_amenity Table
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False, overlaps="place_amenities")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """get linked reviews"""
            reviews_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """get linked Amenities"""
            amenities_list = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, amenity):
            """set linked Amenities"""
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
