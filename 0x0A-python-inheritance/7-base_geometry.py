#!/usr/bin/python3
"""7-base_geometry Module."""


class BaseGeometry:
    """BaseGeometry class."""
    def area(self):
        """Compute area of the class."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value type."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
