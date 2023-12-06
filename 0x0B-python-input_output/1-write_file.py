#!/usr/bin/python3

# 1-write_file.py
"""This modul writes a string to a text file (UTF8) and returns the number
of characters written:"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8) and returns the
    number of characters written:

    Args:
        filename (txt): The file to write to.
        test (str): The text to write in the file
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
