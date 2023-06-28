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

    @property
    def test_width(self):
        """Getter for width"""
        return self.__width

    @test_width.setter
    def test_width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def test_height(self):
        """Getter for height"""

        return self.__height

    @test_height.setter
    def test_height(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def test_x(self):
        """Getter for x"""

        return self.__x

    @test_x.setter
    def test_x(self, value):
        """setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def test_y(self):
        """Getter for y"""

        return self.__y

    @test_y.setter
    def test_y(self, value):
        """setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value


if __name__ == '__main__':
    unittest.main()
