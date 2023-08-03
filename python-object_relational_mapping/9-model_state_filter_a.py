#!/usr/bin/python3
"""
Script tha lists the first States objects from de database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                                                         argv[2],
                                                         argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    s_w_a = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for state in s_w_a:
        print(f'{state.id}: {state.name}')

    session.close()
