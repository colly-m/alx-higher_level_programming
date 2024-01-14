#!/usr/bin/python3
"""
Model script to contail class of a state at an instance
'Base = declarative_base()'
"""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()
"""Defines the base class"""


class State(Base):
    """Attribs:id (int): state id, name (str): state names"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
