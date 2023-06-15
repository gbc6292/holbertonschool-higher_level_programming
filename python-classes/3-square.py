#!/usr/bin/python3
""" File that contain the definition of class Square """


class Square:
    """ square is defined """

    def __init__(self, size=0):
        """size must be an integer and greather than 0"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """Defining area atribute"""

    def area(self):
        a = self.__size * self.__size
        return a
