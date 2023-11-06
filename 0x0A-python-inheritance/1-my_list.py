#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """class MyList that inherits from list and print"""

    def print_sorted(self):
        """
        Print the list in ascending sorted order.
        """
        print(sorted(self))
