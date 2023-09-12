#!/usr/bin/python3
"""defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, "w", encoding="UTF8") as fw:
        fw.write(text)
        with open(filename, "r", encoding="UTF8") as f:
            return len(text)
