#!/usr/bin/python3
"""Module containing the City class"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """
    City class to interact with database id (int): id of classs
    state_id (int): state city belongs to
    name (str): name of class
    """

    __tablename__ = 'cities'


    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
