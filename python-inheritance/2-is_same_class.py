#!/usr/bin/python3
"""function that returns True if the object is exactly an instance
 of the specified class ; otherwise False."""


def is_same_class(obj, a_class):
    """verifying if the obj is a same datype mention in a_class"""
    if type(obj) == a_class:
        """Return whether an object is an instance of a class or of a subclass thereof."""
        return True
    else:
        return False
