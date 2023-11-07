#!/usr/bin/python3
"""This creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
    filename (str): The path to the JSON file to deserialize.

    Returns:
    The Python data structure represented by the JSON string.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
