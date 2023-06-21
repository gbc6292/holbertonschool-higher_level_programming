#!/usr/bin/python3
"""Function that return a list of available
    attributes and methods of an object"""


def lookup(obj):
    """Declaring a variable that contain a list of attributes
    methods"""
    att_method = list(dir(obj))
    return att_method
