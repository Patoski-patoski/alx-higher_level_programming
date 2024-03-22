#!/usr/bin/python3
"""a python file that contains the class definition of a State and an instance
Base = declarative_base():"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Define the Base class
Base = declarative_base()

class State(Base):
    """State inherits from Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

    # Defines the relationship to City
    cities = relationship("City", back_populates="state", cascade="all, delete", passive_deletes=True)
