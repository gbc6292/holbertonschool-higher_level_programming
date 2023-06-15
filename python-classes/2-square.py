#!/usr/bin/python3
""" File that contain the definition of class Square """


class Square:
    """ square is defined """

    def __init__(self, size: int(0)):
        """size must be an integer and greather than 0"""
        if isinstance(size, int):
            raise TypeError('size must be an integer')
        elif isinstance(size) >= 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
