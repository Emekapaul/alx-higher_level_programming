#!/usr/bin/python3

"""8-rectangle modul contains inherited class BaseGeometry and subclass
Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height:

        Args:
            width (str): The width
            height (int): The height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
