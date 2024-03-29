#!/usr/bin/python3
"""Thins module contains the class definition
 of a State and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""State class Definition"""


class State(Base):
    """This class represent a state"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
