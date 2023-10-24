#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
2-square.py: is a Square class that defines a square
"""


class Square:
    """class Square that defines a square
    Attributes:
        attr1 (size): Private instance attribute size
        attr2 (area): area of the square
    """

    def __init__(self, size=0):
        """Initializer with default size = 0"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        area = self.__size * 2
        return(area)
