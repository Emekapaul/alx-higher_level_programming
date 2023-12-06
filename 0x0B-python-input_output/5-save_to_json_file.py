#!/usr/bin/python3

"""5-save_to_json_file modul has func:save_to_json_file(my_obj, filname):"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using a JSON
    representation:

   Args:
    my_obj: The object to write to file as a json sting.
    filename: The file to recieve the json string

    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
