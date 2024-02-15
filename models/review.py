#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """This is the class for Review
    Attributes:
        place_id: Place id
        user_id: User id
        text: Review description
    """
    __tablename__ = "reviews"
    text: str = Column(String(1024), nullable=False)
    place_id: str = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id: str = Column(String(60), ForeignKey("users.id"), nullable=False)
