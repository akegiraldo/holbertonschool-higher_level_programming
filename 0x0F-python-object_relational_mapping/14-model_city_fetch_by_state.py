#!/usr/bin/python3
# Lists all State objects from the database hbtn_0e_6_usa

if __name__ == '__main__':
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    for r in session.query(State, City).filter(City.state_id == State.id):
        print("{}: ({}) {}".format(r.State.name, r.City.id, r.City.name))
