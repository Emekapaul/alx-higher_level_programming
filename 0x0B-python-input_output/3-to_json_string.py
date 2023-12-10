#!/usr/bin/python3

"""3-to_json_string module contains function: to_json_string(my_obj):"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string):

    Args:
        my_obj: The object to serialize
    """
    return json.dumps(my_obj)
