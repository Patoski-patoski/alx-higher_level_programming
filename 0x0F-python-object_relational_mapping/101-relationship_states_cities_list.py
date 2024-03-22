#!/usr/bin/python3
"""a script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker, Session
    from sqlalchemy import create_engine
    from sys import argv
    from relationship_state import Base, State
    from relationship_city import City

    # Create an engine to connect to MySQl server

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create all table for engine
    Base.metadata.create_all(engine)

    # Create a session to link with database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get required data
    # Use join to get both State and City objects
    # Use order_by to sort by states.id and cities.id

    city_and_state = session.query(City, State).join(
            City, State.cities).order_by(State.id, City.id).all()

    # Display results
    current_id = None
    for city, state in city_and_state:
        if current_id is not city.state.id:
            print(f"{city.state.id}: {city.state.name}")
            current_id = city.state.id
        print(f"    {city.id}: {city.name}")

    session.close()
