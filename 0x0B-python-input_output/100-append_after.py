#!/usr/bin/python3
"""define  a function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file
    after each line containing a specific string
    """
    file_text = ""
    with open(filename) as r:
        for file_line in r:
            file_text += file_line
            if search_string in file_line:
                file_text += search_string
    with open(filename, "w") as w:
        w.write(file_text)
