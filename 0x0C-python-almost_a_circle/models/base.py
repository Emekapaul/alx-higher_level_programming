#!/usr/bin/python3

"""The base modul"""


class Base:
    """This class has a base an id:

    Args:
        __nb_objects (int): Its the integer
    """

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
