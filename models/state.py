#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel):
    """ State class """
     __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='delete', backref='state')
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            cities_list = []
            for city in self.cities:
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
