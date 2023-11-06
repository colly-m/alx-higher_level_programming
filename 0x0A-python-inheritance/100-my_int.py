#!/usr/bin/python3
"""Module class MyInt that inherits from int"""


class MyInt(int):
    """A MyInt class body"""

    def __eq__(self, value):
        """Defines value return from equal to not equal to"""
        return (self.real != value)

    def __ne__(self, value):
        """Defines value return from not equal to equal to"""
        return (self.real == value)
