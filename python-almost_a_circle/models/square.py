#!/usr/bin/python3
"""This module defined the Rectangle Class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining the attributes and methods of Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self. width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
