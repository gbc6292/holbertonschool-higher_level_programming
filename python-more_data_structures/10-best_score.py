#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    neededkey = None
    highest_value = float('-inf')
    for key, value in a_dictionary.items():
        if value > highest_value:
            highest_value = value
            neededkey = key
    return neededkey
