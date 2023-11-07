#!/usr/bin/python3
"""This returns the number of characters written."""


def write_file(filename="", text=""):
    """
    Writes a string to a text file using UTF-8 encoding.

    Args:
    filename (str): The path to the file to be written to.
    text (str): The string to write to the file.

    Returns:
    int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        char_written = f.write(text)
        return char_written
