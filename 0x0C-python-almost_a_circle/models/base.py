#!/usr/bin/python3

"""The modul base"""
import json
from os.path import exists


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor:"""

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function that returns the JSON string representation of
        list_dictionaries:"""

        if list_dictionaries is None:
            return "[]"

        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """function  writes the JSON string representation of list_objs to
        a file:"""
        filename = f"{cls.__name__}.json"
        obj_list = []

        if list_objs is None:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("[]")

        else:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())
            with open(filename, "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """Function that returns the list of the JSON string representation
        json_string:"""

        if json_string is None:
            return []

        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Function that returns an instance with all attributes already
        set:"""

        dummy_obj = cls(**dictionary)
        dummy_obj.update(**dictionary)

        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """Function that returns a list of instances:"""
        filename = f"{cls.__name__}.json"

        if not exists(filename):
            return []

        else:
            with open(filename, "r", encoding="utf-8") as f:
                json_contents = cls.from_json_string(f.read())

            return [cls.create(**contents) for contents in json_contents]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """function  writes the JSON string representation of list_objs to
        a file:"""
        filename = f"{cls.__name__}.csv"
        obj_list = []

        if list_objs is None:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("[]")

        else:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())
            with open(filename, "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(obj_list))

    @classmethod
    def load_from_file_csv(cls):
        """Function that returns a list of instances:"""
        filename = f"{cls.__name__}.csv"

        if not exists(filename):
            return []

        else:
            with open(filename, "r", encoding="utf-8") as f:
                json_contents = cls.from_json_string(f.read())

            return [cls.create(**contents) for contents in json_contents]
