#!/usr/bin/python3
"""This returns the dictionary description for json"""


def class_to_json(obj):
    """
    Args:
    obj (object): An instance of a class.

    Returns:
    dictionary representation of json
    """
    return obj.__dict__
