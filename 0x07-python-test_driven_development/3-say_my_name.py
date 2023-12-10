#!/usr/bin/python3

"""The 3-say_my_name defines func: say_my_name(first_name, last_name=""):"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>:

    Args:
        first_name (str): first_name to print.
        last_name (str): last_name to print.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
