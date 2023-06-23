#!/usr/bin/python3
"""
Module that returns the json representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """
    returns a JSON of a string
    """
    json_str = json.dumps(my_obj)
    return json_str
