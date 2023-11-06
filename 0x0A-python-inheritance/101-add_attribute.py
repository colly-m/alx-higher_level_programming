#!/usr/bin/python3
"""Function module to add attributes to an object"""


def add_attribute(obj, attrib, val):
    """Add a new attribute to an object if possible
    Raises: TypeError If attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attrib, val)
