#!/usr/bin/python3

"""This modul defines a square rectangle"""


class Rectangle:
    """This class defines a square rectangle"""

    def __init__(self, width=0, height=0):
        """It instantiates the object

        Args:
            width (int): The value assigned to the obect attribute
            height (int): The value assigned to the obect attribute

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """It retrieves/returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """It initializes/assigns the new value to self.__width

        Args:
            value (int): new value to assign to object attribute

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif (value < 0):
            raise ValueError("width must be >= 0")

        else:
            self.__width = value

    @property
    def height(self):
        """It retrieves/returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """It initializes/assigns the new value to self.__height

        Args:
            value (int): new value to assign to object attribute

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif (value < 0):
            raise ValueError("height must be >= 0")

        else:
            self.__height = value
