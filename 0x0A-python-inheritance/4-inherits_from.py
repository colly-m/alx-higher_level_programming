#!/usr/bin/python3
"""Function to check if objecr is instance of a class"""


def inherits_from(obj, a_class):
    """Base case: if pbj is an instance of a class returns True"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
