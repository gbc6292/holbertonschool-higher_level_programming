#!/usr/bin/python3
"""This module defined the Rectangle Class"""
import unittest

from test_base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def test__init__(self, width, height, x=0, y=0, id=None):
        """Asigning arguments to the right attribute"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def testget_width(self):
        """Getter for width"""
        return self.__width

    def testset_width(self, value):
        """Setter for width"""
        if value <= 0:
            raise ValueError("Width must be greater than zero.")
        self.__width = value

    def testget_height(self):
        """Getter for height"""

        return self.__height

    def testset_height(self, value):
        """Setter for width"""
        if value <= 0:
            raise ValueError("Height must be greater than zero")
        self.__height = value

    def testget_x(self):
        """Getter for x"""

        return self.__x

    def testset_x(self, value):
        """setter for x"""
        if value < 0:
            raise ValueError("x can't be negative")
        self.__x = value

    def testget_y(self):
        """Getter for y"""

        return self.__y

    def testset_y(self, value):
        """setter for y"""
        if value < 0:
            raise ValueError("y can't be negative")

        self.__y = value


if __name__ == '__main__':
    unittest.main()
