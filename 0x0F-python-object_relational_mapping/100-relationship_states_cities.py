#!/usr/bin/python3
"""Script to create "California" 'State' with the city 'San Francisco'"""


from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    """Accesses the database server"""
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])

    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    n_state = State(name='California')
    n_city = City(name='San Franscisco')
    n_state.cities.append(n_city)

    session.add(n_state)
    session.commit()
    session.close()
