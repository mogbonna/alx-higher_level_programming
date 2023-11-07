#!/usr/bin/python3
"""Returns Python data structure."""
import json


def from_json_string(my_str):
    """
    Args:
    my_str (str): The JSON string to deserialize.

    Returns:
    The Python data structure.
    """
    return json.loads(my_str)
