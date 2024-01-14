#!/usr/bin/python3
"""Script to add 'State' object 'Louisiana' to 'hbtn_0e_6_uas'"""


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

    state_update = session.query(State).filter_by(id=2).first()
    state_update.name = 'New Mexico'

    session.commit()

    session.close()
