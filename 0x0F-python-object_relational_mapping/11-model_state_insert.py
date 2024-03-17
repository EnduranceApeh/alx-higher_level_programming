#!/usr/bin/python3
"""
A script thatg get State objects that have 'a' from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get first state object from database
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print("{:d}".format(new_state.id))

    session.close()
