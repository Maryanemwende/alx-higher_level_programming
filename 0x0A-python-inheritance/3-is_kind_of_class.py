#!/usr/bin/python3
"""define a function that checks the class"""


def is_kind_of_class(obj, a_class):
    """checks if :if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class. object is the objectto check
    a_class is the class to match the object to
    Return True if it is, False if not
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
