#!/usr/bin/python3
"""define a function that checks the class"""


def is_same_class(obj, a_class):
    """check if the object is exactly an instance of the class
    obj is the object to check
    a_class is the class to match the object to
    returns True if the object is exactly an instance of a_class
    returns False if its not
    """
    if type(obj) == a_class:
        return True
    else:
        return False
