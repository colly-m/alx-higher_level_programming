#!/usr/bin/python3
"""Script to list all city objects from database 'hbtn_0e_101_usa'"""


from relationship_state import Base, State
from relationship_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """Accesses the database server"""
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])

    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    statesNcities = (session.query(State).join(City).order_by(City.id).all())

    for state in statesNcities:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
