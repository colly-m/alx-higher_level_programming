#!/usr/bin/python3
"""Function defines class that inherits from list"""


class MyList(list):

    def print_sorted(self):
        """Defines instance to print the list in ascending sort"""
        sorted_list = sorted(self)
        print(sorted_list)
