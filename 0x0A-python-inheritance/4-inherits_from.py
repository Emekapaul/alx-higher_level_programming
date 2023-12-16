#!/usr/bin/python3

"""4-inherits_from contains the function: inherits_from(obj, a_class)"""


def inherits_from(obj, a_class):
    """function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False.

    Args:
        obj: The object or the insinstance of the class
        a_class: The class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
