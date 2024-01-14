#!/usr/bin/python3
"""Script to delete all 'State' objects with 'a' from 'hbtn_0e_6_usa'"""


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

    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    for state in states_with_a:
        session.delete(state)

    session.commit()

    session.close()
