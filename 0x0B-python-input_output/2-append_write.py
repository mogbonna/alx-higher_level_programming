#!/usr/bin/python3
"""This returns the number of characters added."""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8)
    If the file does not exist, it will be created.

    Args:
    filename (str): The path to the file to be appended to.
    text (str): The string to append to the file.

    Returns:
    The number of characters that were appended.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
