#!/usr/bin/python3
"""This returns the JSON representation of an object as a string."""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
    my_obj (Any): The object to serialize to a JSON-formatted str.

    Returns:
    str: JSON representation of my_obj.
    """
    return json.dumps(my_obj)
