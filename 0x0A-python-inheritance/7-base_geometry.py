#!/usr/bin/python3
"""defines a class BaseGeometry"""


class BaseGeometry:
    """represents class BaseGeometry"""

    def area(self):
        """raises an Exception - area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value, assume name is always a string
        if value is not an integer: raise a TypeError exception
        if value is less or equal to 0: raise a ValueError
        """
        if type(value) != int:
            raise TypeError("<name> must be an integer".format(name))
        if value <= 0:
            raise ValueError("<name> must be greater than 0".format(name))
