#!/usr/bin/python3
"""  a script that lists all City objects from the database hbtn_0e_101_usa"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session, sessionmaker
    from relationship_city import City
    from relationship_state import Base, State

    # Create an engine to connect with the MySQL server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create all table for enine
    Base.metadata.create_all(engine)

    # Create a session to interact with database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get data
    my_city = session.query(City).order_by(City.id).all()

    for state_rel_ship in my_city:
        print(f"{state_rel_ship.id}: {state_rel_ship.name} -> {state_rel_ship.state.name}")

    session.close()
