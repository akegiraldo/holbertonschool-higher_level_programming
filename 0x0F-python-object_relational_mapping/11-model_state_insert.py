#!/usr/bin/python3
# Lists all State objects from the database hbtn_0e_6_usa

if __name__ == '__main__':
	from model_state import Base, State
	from sqlalchemy.orm import sessionmaker
	from sqlalchemy import (create_engine)
	from sys import argv

	engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

	Session = sessionmaker(bind=engine)
	Session.configure(bind=engine)
	session = Session()

	new_state = State(name='Louisiana')
	session.add(new_state)
	print (new_state.id)
