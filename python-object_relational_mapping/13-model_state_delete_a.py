#!/usr/bin/python3
"""
Script tha lists the name of State objects passed as an
argument from de database hbtn_0e_6_usa"""

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

    state_to_delete = session.query(State).filter(
        State.name.ilike('%a%')).all()

    for state in state_to_delete:
        session.delete(state)
    session.commit()

    session.close()
