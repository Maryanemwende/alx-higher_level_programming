#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents class Rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height

        width and height must be private. No getter or setter
        width and height must be positive integers,
        validated by integer_validator
        """

        super().integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        super().__height = height

    def area(self):
        """finds area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """print() should print, and str() should return
        [Rectangle] <width>/<height>"""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
