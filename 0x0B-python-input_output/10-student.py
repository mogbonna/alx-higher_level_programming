#!/usr/bin/python3
"""Retrieves a dictionary representation of a Student instance."""


class Student:
    """
    Defines a Student Class
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiates a Student object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns:
        A dictionary containing key/value pairs of attributes.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
