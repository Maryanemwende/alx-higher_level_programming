#!/usr/bin/python3
"""defines a function that reads text from file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="UTF8") as f:
        for line in f:
            print(line, end="")
