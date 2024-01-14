#!/usr/bin/python3
"""Script to list all State objects and corresponding City objects"""


from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine, Column, Integer, String, ForeignKey)
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sys import argv


if __name__ == '__main__':
    """Accesses the database server"""
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])

    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    query_result = (session.query(State)
                    .outerjoin(City)
                    .order_by(State.id, City.id)
                    .all())

    for state in query_result:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
