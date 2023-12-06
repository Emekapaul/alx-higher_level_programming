#!/usr/bin/python3

"""This 0-add_integer modul defines the function add_integer(a, b=98):"""

def add_integer(a, b=98):
    """function that adds 2 integers:

    Args:
        a (int | float): Accepts int or float values.
        b (int | float): Accepts int or float values.

    Returns:
        int. Floats are typecasted to int before it's returned.
    """
    if isinstance(a, float) or isinstance(b, float):
        return int(a) + int(b)

    if not isinstance(a, int) or isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
