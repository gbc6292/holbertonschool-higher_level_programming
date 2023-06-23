#!/usr/bin/python3
"""
Module that returns an object (Python data structure)
represented by a json string
"""
import json

def from_json_string(my_str):
    """returns an object by a json string."""
    return json.loads(my_str)
