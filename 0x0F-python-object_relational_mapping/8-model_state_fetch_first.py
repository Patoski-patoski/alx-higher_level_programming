#!/usr/bin/python3
"""  a script that prints the first State object from the database
hbtn_0e_6_usa"""

if __name__ == "__main__":
    from sqlalchemy import (create_engine)
    from sys import argv
    from sqlalchemy.orm import sessionmaker

    from model_state import Base, State

    # Create an engine to conncet to MySQl server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create all tables for the engine
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query first state
    first_state = session.query(State).first()

    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))
