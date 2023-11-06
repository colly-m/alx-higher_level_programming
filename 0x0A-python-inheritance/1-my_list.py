#!/usr/bin/python3
"""Function defines class that inherits from list"""


class MyList(list):
    """Class that inherits from a list"""
    def print_sorted(self):
        """Defines instance to print the list in ascending sort"""
        print(sorted(self))
