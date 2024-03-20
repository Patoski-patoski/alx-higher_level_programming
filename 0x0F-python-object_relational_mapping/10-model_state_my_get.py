#!/usr/bin/python3
"""  a script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    from model_state import Base, State

    # Create engine to connect to the MySql server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3600/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create all table in the engine
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states from command line
    cmd_arg = argv[4]
    states = session.query(State).filter(State.name == cmd_arg).order_by(
            State.id.asc()).all()

    if states:
        for state in states:
            print(state.id)
    else:
        print("Not found")
