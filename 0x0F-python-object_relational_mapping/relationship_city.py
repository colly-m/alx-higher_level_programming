#!/usr/bin/python3
"""Script to define a City class working with MySQLAlchemy ORM"""


from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
    Defines a city class:
    id (int): The id of the class, name (str): The name of the class
    state_id (int): The state the city belongs in
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
