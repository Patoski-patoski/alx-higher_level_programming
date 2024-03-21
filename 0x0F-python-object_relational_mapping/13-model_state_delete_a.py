#!/usr/bin/python3
"""a script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, Session

    from sys import argv

    from model_state import Base, State

    # Create an engine to connect to the MySQL server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create all tables for engine
    Base.metadata.create_all(engine)

    # Create sessions to inteact with database
    Session = sessionmaker(bind=engine)
    session = Session()

    # remove a record in the state table
    session.query(State).filter(
            State.name.like("%a%")
            ).delete(synchronize_session="fetch")

    session.commit()
