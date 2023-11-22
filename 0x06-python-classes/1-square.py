#!/usr/bin/python3

# 1-square.py
"""This module defines a class Square. The private instance attribute is
    _size, initializes it with size (no type/value verification)
"""


class Square:
    """Defines a class Square and has __init__ method"""

    def __init__(self, size):
        """Istantiates the object attribute

        Args:
            size (int): Instantiation with size
            (no type/value verification)
        """
        self.__size = size
