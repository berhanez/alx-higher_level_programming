#!/usr/bin/python3
"""Defining a str to JSON function."""
import json


def save_to_json_file(my_obj, filename):
    """ Returns the JSON representation of a string object."""
    return json.dumps(my_obj)
