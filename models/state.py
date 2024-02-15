#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities_list = relationship("City", cascade='all, delete, delete-orphan',
                               backref="state")

    @property
    def cities(self):
        """Getter method for cities"""
        return [city for city in models.storage.all(City).values()
                if city.state_id == self.id]
