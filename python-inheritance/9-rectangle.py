#!/usr/bin/python3
"""Creating a empty class"""


class BaseGeometry():
    """Creating a public instance method"""

    def area(self):
        """Adding an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate if the value is an integer and greater than 0"""

        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise TypeError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    """A child class from Base Geometry"""

    def __init__(self, width, height):
        """Creating instance for width and height
        and validate that the argument are integers"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """This Method return the area the
        area of a rectangle multiplyin the
        values of width and height"""
        return self.__width * self.__height

    def __str__(self):
        """printing rectangle descriptions"""
        return f"[Rectangle] {self.__width}/{self.__height}"
