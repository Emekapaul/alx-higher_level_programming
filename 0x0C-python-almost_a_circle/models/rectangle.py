#!/usr/bin/python3
"""The rectangle modul"""

from models.base import Base


class Rectangle(Base):
    """Class rectangle that inherits from base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor: """
        Base.__init__(self, id)
        """constructor for inherited class"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter function for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter function for width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        """Getter function for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter function for height"""

        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """Getter function for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter function for x"""

        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """Getter function for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter function for y"""

        if type(y) is not int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """function that computes the area"""

        return self.__width * self.__height

    def display(self):
        """It prints rectangle instance to stdout"""

        print(end="\n" * self.__y)
        for h in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width, end="")
            print()

    def __str__(self):
        """Function that prints to stdout"""

        return f"[{type(self).__name__}] ({self.id}) {self.__x}/{self.__y} - "\
               f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Function that updates the class rectangle"""
        upd_attributes = ["id", "width", "height", "x", "y"]

        if args is not None:
            for i, value in enumerate(args):
                if i < len(upd_attributes):
                    setattr(self, upd_attributes[i], value)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """function returns dictionary representation of a Rectangle:"""

        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
