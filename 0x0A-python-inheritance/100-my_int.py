#!/usr/bin/python3
"""Define a class"""


class MyInt(int):
    """
    class MyInt that inherits from int
    """
    def __eq__(self, value):
        """define instances"""
        return super().__ne__(value)

    """define a function"""
    def __ne__(self, value):
        """define instances"""
        return super().__eq__(value)
