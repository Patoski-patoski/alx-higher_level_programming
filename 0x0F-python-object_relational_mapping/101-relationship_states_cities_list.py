#!/usr/bin/python3
"""Lists all State objects and corresponding City objects contained in the
database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City

    # Establish MySQL connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create all tables
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all states
    states_and_cities = session.query(State, City).join(
        City, State.cities).order_by(State.id, City.id).all()

    current_state_id = None
    for state, city in states_and_cities:
        if state.id != current_state_id:
            print(f"{state.id}: {state.name}")
            current_state_id = state.id
        print(f"    {city.id}: {city.name}")

    session.close()
