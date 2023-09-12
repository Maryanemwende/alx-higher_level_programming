#!/usr/bin/python3
"""defines function that appends a string at end of a text file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    returns the number of characters added
    """
    with open(filename, "a", encoding="UTF8") as f:
        f.write(text)
        with open(filename, "r", encoding="UTF8") as fn:
            return len(text)
