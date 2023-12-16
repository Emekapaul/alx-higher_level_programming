#!/usr/bin/python3

"""Modul 0-lookup contains function: lookup(obj)"""


def lookup(obj):
    """function that returns the list of available attributes and methods
    of an object:

    Args:
        obj: The object / instance
    """

    return dir(obj)
