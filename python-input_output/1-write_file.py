#!/usr/bin/python3
""" Module of write file """


def write_file(filename="", text=""):
    """ Write a text into a  file """
    with open(filename, 'w') as f:
        return (f.write(text))
