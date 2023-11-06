#!/usr/bin/python3
"""Function to check if object is an instance or class instance"""


def is_kind_of_class(obj, a_class):
    """Defines the class an object belongs to or if object is a class"""
    if isinstance(obj, a_class):
        return (True)
    return (False)
