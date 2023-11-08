#!/usr/bin/python3
"""Function to return class-to-JSON module object"""


def class_to_json(obj):
    """Returns dictionary description of json."""
    return (obj.__dict__)
