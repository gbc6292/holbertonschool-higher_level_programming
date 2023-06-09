#!/usr/bin/python3
""" File that contain the definition of class Square """


class Square:
    """Initializing the class Square"""

    def __init__(self, size=0):
        """ square is defined """
        self.size = size

    @property
    def size(self):
        """Return the private instance 'size'"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the value from the private instance size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Defining area atribute"""
        a = self.size * self.size
        return a

    def my_print(self):
        """Printing the square using '#' character"""
        if self.size == 0:
            print()
        else:
            for x in range(self.size):
                for y in range(self.size):
                    print('#', end='')
                print()
