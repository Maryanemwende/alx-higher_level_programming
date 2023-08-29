#!/usr/bin/python3

"""defining a class Square"""


class Square:
    """data represantation of class Square"""

    def __init__(self, size=0):
        """initializing attributes of Square.
        self is the parameter to refer to an instance of Square,
        size is the size of Square - data attribute"""

        self.size = size

    @property
    def size(self):
        """retrieves current size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area of Square"""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""
        for x in range(0, self.__size):
            [print("#", end="")for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
