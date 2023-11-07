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
    
    # The json module is used for deserialization from JSON.
    # The loads method deserializes my_str to a Python object.
    return json.loads(my_str)
