#!/usr/bin/python3

"""Modul 3-is_kind_of_class has function: is_kind_of_class(obj, a_class)"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance of, or if
    the object is an instance of a class that inherited from, the specified
    class; otherwise False.

    Args:
        obj: The object / instance
        a_class: The class
    """

    return isinstance(obj, a_class)
