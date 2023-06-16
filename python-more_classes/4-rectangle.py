#!/usr/bin/python3

"""class rectangle"""


class Rectangle:
    """Rectangle defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """returning the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """adding the value to width if is a int"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """adding the value to height if is a int"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function that return the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """function that return the perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """function that print rectangle or a empty string"""
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for _ in range(self.__height):
            string += "#" * self.__width + "\n"
        return string.rstrip()

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
