#!/usr/bin/python3
"""This module defined the Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Asigning arguments to the right attribute"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        """Getter for width"""
        return self.__width

    def set_width(self, value):
        """Setter for width"""
        if value <= 0:
            raise ValueError("Width must be greater than zero.")
        self.__width = value

    def get_height(self):
        """Getter for height"""

        return self.__height

    def set_height(self, value):
        """Setter for width"""
        if value <= 0:
            raise ValueError("Height must be greater than zero")
        self.__height = value

    def get_x(self):
        """Getter for x"""

        return self.__x

    def set_x(self, value):
        """setter for x"""
        if value < 0:
            raise ValueError("x can't be negative")
        self.__x = value

    def get_y(self):
        """Getter for y"""

        return self.__y

    def set_y(self, value):
        """setter for y"""
        if value < 0:
            raise ValueError("y can't be negative")

        self.__y = value
