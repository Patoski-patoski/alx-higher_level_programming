#!/usr/bin/python3
""" a script that adds the State object “Louisiana” to the database
hbtn_0e_6_usa"""

if __name__ == "__main__":

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    from model_state import Base, State

    # Create an engine to connect to the MySQL server

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # add a new Object Louisiana
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)
