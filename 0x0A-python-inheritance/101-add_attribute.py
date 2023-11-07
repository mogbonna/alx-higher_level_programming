#!/usr/bin/python3
"""101-add_attribute.py: Can I?"""


def add_attribute(self, name, new):
    """This Function adds a new attribute to an object if possible"""
    try:
        self.name = new
    except:
        raise TypeError("can't add new attribute")
