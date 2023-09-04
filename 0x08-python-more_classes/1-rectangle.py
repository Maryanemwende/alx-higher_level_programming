#!/usr/bin/python3

"""define a class Rectangle"""


class Rectangle:
    """data representation of class Rectangle"""

    def __init__(self, width=0, height=0):
        """initializing attributes of Rectangle class

        self is a parameter to refer to an instance of the class
        width is the width of the rectangle - an integer
        height is the height of the rectangle - an integer"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Private instance attribute that retrieves the width"""
        return self.___width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Private instance attribute that retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

