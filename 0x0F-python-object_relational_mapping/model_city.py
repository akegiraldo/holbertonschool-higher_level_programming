#!/usr/bin/python3
# model city

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from model_state import Base
from sqlalchemy import ForeignKey


class City(Base):
        __tablename__ = 'cities'
        id = Column(Integer, primary_key=True)
        name = Column(String(128), nullable=False)
        state_id = Column('state_id', Integer, ForeignKey("states.id"),
                          nullable=False)
