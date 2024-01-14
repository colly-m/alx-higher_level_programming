#!/usr/bin/python3
"""Script to delete all 'State' objects with 'a' from 'hbtn_0e_6_usa'"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == '__main__':
    """Accesses the database server"""
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])

    engine = create_engine(url)
    Session = sessionmaker(bind=engine)

    session = Session()

    result = (session.query(State, City)
              .filter(State.id == City.state_id)
              .order_by(City.id).all())

    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()

    session.close()
