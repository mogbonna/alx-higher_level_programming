#!/usr/bin/python3
"""
Retrieve a list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns:
        A list of attribute and method names of the object.
    """
    return dir(obj)
