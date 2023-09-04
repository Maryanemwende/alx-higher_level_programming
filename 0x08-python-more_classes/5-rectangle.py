#!/usr/bin/python3

"""Define a class - Rectangle"""


class Rectangle:
    """representation of the class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing attributes of class Rectangle

        self is a parameter to refer to an instance of Rectangle
        width is the width of the rectangle - integer
        height is the height of the rectangle - integer
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Private instance attribute that retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print the rectangle with the character #
        returns the printable representation of rectangle

        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for x in range(self.__height):
            [rectangle.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        """return string representation of Rectangle"""

        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        """prints bye rectangle every time rectangle is deleted"""

        print("Bye rectangle...")
