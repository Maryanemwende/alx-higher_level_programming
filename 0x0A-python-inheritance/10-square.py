#!/usr/bin/python3
"""Define class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents class square"""

    def __init__(self, size):
        """size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
