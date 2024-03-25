#!/usr/bin/python3
"""Write a Python file similar to model_state.py named
model_city.py that contains the class definition of a City."""

from sqlalchemy import String, Column, Integer, ForeignKey
from model_state import Base, State


class City(Base):
    """Defines a City class mapped to a city table."""
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
