#!/usr/bin/python3

"""4-from_json_string module contains function: from_json_string(my_str)"""
import json


def from_json_string(my_str):
    """function that returns an object (Python data structure) represented
    by a JSON string:

    Args:
        my_str: The json string to return to Python data structure
    """

    return json.loads(my_str)
