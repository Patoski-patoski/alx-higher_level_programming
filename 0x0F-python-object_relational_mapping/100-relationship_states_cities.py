#!/usr/bin/python3
""" a script that creates the State “California” with the City “San Francisco”
from the database"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, Session
    from sys import argv
    from relationship_state import Base, State
    from relationship_city import City

    # Create an engine to interact with the MySQL server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create table for all engines
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new object from State
    california = State(name="California")
    session.add(california)
    session.commit()

    # Create new object from City
    san_francisco = City(name="San Francisco", state=california)
    session.add(san_francisco)
    session.commit()

    session.close()
