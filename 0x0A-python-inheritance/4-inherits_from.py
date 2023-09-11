#!/usr/bin/python3
"""define a function that checks for inherited class"""


def inherits_from(obj, a_class):
    """checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    obj is the object to check
    a_class is the class to match it to
    Return true if it does, False if not
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
