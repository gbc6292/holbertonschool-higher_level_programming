#!/usr/bin/python3
"""function that returns True if the object is an instance of,
 or if the object is an instance of a class that inherited from, """


def is_kind_of_class(obj, a_class):
    """Return whether an object is an instance
    of a class or of a subclass thereof."""
    return isinstance(obj, a_class)
