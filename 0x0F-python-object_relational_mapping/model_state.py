#!/usr/bin/python3
"""Write a python file that contains the class definition
of a State and an instance Base = declarative_base():"""

from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """Defines a State class mapped to a state table."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
