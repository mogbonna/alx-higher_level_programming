#!/usr/bin/python3
"""
Check if the given object is an instance of, or
inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or its subclasses;
        False otherwise.
    """
    return isinstance(obj, a_class)
