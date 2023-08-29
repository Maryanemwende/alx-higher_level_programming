#!/usr/bin/python3

"""define a class Square"""


class Square:
    """data represenation of the class Square"""

    def __init__(self, size=0):
        """Initializing attributes of Square.
        self is the parameter to refer to an instance of square,
        size is a data attribute - size of the square."""

        self.__size = size
