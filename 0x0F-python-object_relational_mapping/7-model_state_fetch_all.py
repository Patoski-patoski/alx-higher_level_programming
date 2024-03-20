#!/usr/bin/python3
"""a script that lists all State objects from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    from sqlalchemy import (create_engine)

    # Create an engine that cnnects to the MySQL server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all state
    states = session.query(State).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
