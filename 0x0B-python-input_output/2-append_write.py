#!/usr/bin/python3

# 2-append_write.py
"""This modul appends a string at the end of a text file (UTF8) and returns
the number of characters added:"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8) and
    returns the number of characters added:

    Args:
        filename (txt): The file to append text to.
        test (str): The text to append in the file
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
