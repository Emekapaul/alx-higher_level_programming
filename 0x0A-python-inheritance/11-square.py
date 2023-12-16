#!/usr/bin/python3

"""Module 10-square contains class square that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The class Square"""

    def __init__(self, size):
        """Instantiation with size"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Function to get the area of rectangle"""

        return self.__size * self.__size

    def __str__(self):
        """Funtionn that prints"""

        return "[Square] {}/{}".format(self.__size, self.__size)
