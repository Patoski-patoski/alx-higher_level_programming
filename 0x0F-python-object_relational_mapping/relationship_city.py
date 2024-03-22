#!/usr/bin/python3
"""Start link class to table in database
"""
from relationship_state import Base, relationship
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):

    """ Creates a class definition: city"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    # Define relationship between State
    state = relationship("State", back_populates="cities")
