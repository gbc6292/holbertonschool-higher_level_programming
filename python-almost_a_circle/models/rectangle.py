#!/usr/bin/python3
"""This module defined the Rectangle Class"""

from base import Base

class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__id = id
        super().__init__(id)

