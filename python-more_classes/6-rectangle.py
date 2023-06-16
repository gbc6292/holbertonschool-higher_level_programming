#!/usr/bin/python3

"""class rectangle"""


class Rectangle:
    """Rectangle defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Method that initializes the instances"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """function that calculates the perimeter"""
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
        """Method that returns the string represantion of the instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Method that prints a message when the instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
