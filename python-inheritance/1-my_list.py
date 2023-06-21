#!/usr/bin/python3
"""Defining a SuperClass named MyList"""


class MyList(list):
    """Creating a new sorted list
    and printed"""

    def print_sorted(self):
        """save the new list into a variable"""
        sorted_list = sorted(self)
        print(sorted_list)
