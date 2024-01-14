#!/usr/bin/python3
"""Script to list all 'State' objects containing 'a' from 'hbtn_0e_6_usa'"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    """Accesses the database server"""
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])

    engine = create_engine(url)
    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(State).filter(State.name.like('%a%'))
    states = query.all()

    for state in states:
        print('{0}: {1}'.format(state.id, state.name))
