#!/usr/bin/python3
"""Creating a empty class"""

BaseGeometry = __import__('9-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """A child class from BaseGeometry"""

    def __init__(self, width, height):
        """Set width and height and validate
        that the argument are positive integers"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
