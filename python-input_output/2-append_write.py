#!/usr/bin/python3
"""
Module that returns the JSON representation of an object (string):
"""


def append_write(filename="", text=""):
    """ Append text into a  file """
    with open(filename, 'a') as f:
        return f.write(text)
