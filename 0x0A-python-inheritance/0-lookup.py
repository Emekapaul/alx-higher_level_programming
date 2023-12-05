#!/usr/bin/python3

#0-lookup.py
"""This modul provides list of available attributes and methods"""


def lookup(obj):
    """function that returns the list of available attributes and methods
    of an object

    Args:
        obj: class attibutes


    """
    return dir(obj)
