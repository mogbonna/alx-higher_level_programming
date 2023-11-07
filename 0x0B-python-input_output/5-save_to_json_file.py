#!/usr/bin/python3
"""This writes an object to a text file."""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
    my_obj (Any): The object to serialize and write to the file.
    filename (str): The path to the file to be saved.

    Returns:
    None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
