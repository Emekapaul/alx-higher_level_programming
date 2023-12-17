#!/usr/bin/python3
"""Modul that contains class Square which inherits from class Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor: """

        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """The function to print to stdout"""

        return f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y}"\
               f" - {self.width}"

    @property
    def size(self):
        """Getter function for size"""
        return self.width

    @size.setter
    def size(self, size):
        """setter function for size"""

        if type(size) is not int:
            raise TypeError("width must be an integer")

        if size <= 0:
            raise ValueError("width must be > 0")

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update function that assigns attribute"""

        upd_attributes = ["id", "size", "x", "y"]

        if args is not None:
            for i, value in enumerate(args):
                if i < len(upd_attributes):
                    setattr(self, upd_attributes[i], value)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Function that returns dictionary representation of a square"""

        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
