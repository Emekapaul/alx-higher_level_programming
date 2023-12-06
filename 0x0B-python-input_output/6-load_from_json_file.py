#!/usr/bin/python3

"""6-load_from_json_file modul has func: 0load_from_json_file(filename):"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”:

    Args:
        filename: The file to read the json strimh from.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
