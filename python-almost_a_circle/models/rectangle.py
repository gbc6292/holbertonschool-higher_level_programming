#!/usr/bin/python3
"""This module defined the Rectangle Class"""

from typing import Any
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__id = id
        super().__init__(id)

    def get_width(self):
        return self.__width

    def set_width(self, value):
        self.width = value

    def get_height(self):
        return self.__height

    def set_height(self, value):
        self.height = value

    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value
