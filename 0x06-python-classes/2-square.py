#!/usr/bin/python3

"""define a class Square"""


class Square:
    """data represenation of the class Square"""

    def __init__(self, size=0):
        """Initializing attributes of Square.
        self is the parameter to refer to an instance of square,
        size is a data attribute - size of the square."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
