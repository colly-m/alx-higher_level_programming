#!/usr/bin/python3
"""
Script to print 'State' object with 'name' as argument from
database 'hbtn_0e_6_usa'
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    """Accesses the database server"""
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])

    engine = create_engine(url)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.name == argv[4]).first()

    if state is not None:
        print('{0}'.format(state.id))
    else:
        print('Not found')
