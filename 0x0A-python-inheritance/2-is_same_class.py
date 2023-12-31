#!/usr/bin/python3
"""Check if the given object is exactly an instance of the specified class."""


def is_same_class(obj, a_class):
    """
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class; False otherwise.
    """
    return type(obj) is a_class
