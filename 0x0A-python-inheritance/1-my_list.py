#!/usr/bin/python3
"""define a class MyList that inherits from list"""


class MyList(list):
    """implements sorted printing for class List"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
