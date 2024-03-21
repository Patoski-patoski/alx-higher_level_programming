#!/usr/bin/python3
"""a script that changes the name of a State object from the database
hbtn_0e_6_usa"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sys import argv
    from sqlalchemy.orm import sessionmaker, Session

    from model_state import Base, State

    # Create an engine to be linked t the MySQl server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create all tables for engine
    Base.metadata.create_all(engine)

    # Create a session to interact with MySQL
    Session = sessionmaker(bind=engine)
    session = Session()

    # query that changes the name of a State object
    update_name = session.query(State).filter(State.id == 2).first()

    if update_name:
        new_name = "New Mexico"
        update_name.name = new_name

    session.commit()
    session.close()
