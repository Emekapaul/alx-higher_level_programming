#!/usr/bin/python3

# 4-square.py
"""This module defines a class, creates and initializes an instance"""


class Square:
    """A class that defines a square and also creates an object"""

    def __init__(self, size=0):
        """It instantiates the objec

        Args:
            size (int): The size of square

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

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """It retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """It sets/updates the value of the object attribute

        Args:
            value (int): The new value to initialize to the object attri

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
