#!/usr/bin/python3

# 0-read_file.py
"""This modul reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout:

    Args:
        filename (str): The file to read from.

    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
