#!/usr/bin/python3
"""Function to return validity of a class instance"""


def is_same_class(obj, a_class):
    """Checks if an object is instance in a given class
    Returns: Boolean of an instance of class
    """
    if type(obj) == a_class:
        return (True)
    return (False)
