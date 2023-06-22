#!/usr/bin/python3
"""function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class ; otherwise False."""


def inherits_from(obj, a_class):
    """Return whether an object is an instance of a class or of a subclass thereof."""
    return isinstance(obj, a_class) and type(obj) is not a_class
