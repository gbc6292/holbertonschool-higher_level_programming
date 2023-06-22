#!/usr/bin/python3
"""Creating a empty class"""


class BaseGeometry():
    """Creating a public instance method
    """

    def area(self):
        """adding an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f'{name}must be an integer')
        elif value <= 0:
            raise TypeError(f"{name} must be greater than 0")
