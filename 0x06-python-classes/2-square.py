#!/usr/bin/python3

# 2-square.py
"""This module defines a class, creates and initializes an instance"""


class Square:
    """A class that defines a square and also creates an object"""

    def __init__(self, size=0):
        """It instantiates the object

        Args:
            size (int) = The size of square

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
