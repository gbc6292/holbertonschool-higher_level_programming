#!/usr/bin/python3
"""Creating a empty class"""


class BaseGeometry():
    """Creating a public instance method"""

    def area(self):
        """Adding an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate if the value is an integer and greater than 0"""
        if isinstance(name, str):
            if type(value) is not int:
                raise TypeError(f'{name} must be an integer')
            elif value <= 0:
                raise TypeError(f'{name} must be greater than 0')
