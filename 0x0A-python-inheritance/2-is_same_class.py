#!/usr/bin/python3

"""Modul 2-is_same_class has func: is_same_class(obj, a_class)"""


def is_same_class(obj, a_class):
    """function that returns True if the object is exactly an instance of
    the specified class ; otherwise False.

    Args:
        obj: The object or insintance of the class
        a_class: The class
    """

    if type(obj) == a_class:
        return True

    else:
        return False
