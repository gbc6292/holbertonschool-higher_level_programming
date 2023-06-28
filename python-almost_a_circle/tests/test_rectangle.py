#!/usr/bin/python3
"""This module defined the Rectangle Class"""
import unittest

from test_base import Base


class Rectangle(unittest.TestCase):
    """Rectangle Class"""

    def test__init__(self, width, height, x=0, y=0, id=None):
        """Attributes of the class rectangle class"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__id = id
        super().__init__(id)


if __name__ == '__main__':
    unittest.main()
