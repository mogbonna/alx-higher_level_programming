#!/usr/bin/python3
"""A class Student that defines a student"""


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
        Retrieves a dictionary representation.

        Returns:
        A dictionary containing key/value pairs of attributes.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
        A dictionary where keys and values of the public attributes.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
