#!/usr/bin/python3
""" Module of add item """

import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


def main():
    """ add a json item into a new file """
    try:
        new_load = load_from_json_file('add_item.json')
    except:
        new_load = []
    for i in range(0, len(sys.argv)):
        if i != 0:
            new_load.append(sys.argv[i])
    save_to_json_file(new_load, 'add_item.json')
