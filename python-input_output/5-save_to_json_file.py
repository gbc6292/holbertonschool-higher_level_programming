#!/usr/bin/python3
"""
Module writes an Object to a text file, using a json representation
"""
import json

def save_to_json_file(my_obj, filename):
    """
    Function that writes an object using a
    JSON representation.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
