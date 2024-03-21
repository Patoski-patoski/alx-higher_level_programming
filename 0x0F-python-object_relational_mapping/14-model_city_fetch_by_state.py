#!/usr/bin/python3
""" a Python file similar to model_state.py named model_city.py that contains
the class definition of a City. 
A script 14-model_city_fetch_by_state.py that prints all City objects from the
database hbtn_0e_14_usa:"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sys import argv
    from sqlalchemy.orm import sessionmaker, Session
    from model_state import Base, State
    from model_city import City


    # Create the engine to connect to the MySQL server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create all tables from engine
    Base.metadata.create_all(engine)

    # Create sessions to interact with database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get required data
    cities = session.query(City).join(
            State).order_by(City.id.asc()).all()

    for city in cities:
        print(f"{city.states.name}: ({city.id}) {city.name}")

    session.close()
