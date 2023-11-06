#!/usr/bin/python3
"""Function to return list of available attributes and methods"""


def lookup(obj):
    """Returns a list object of available attributes and methods of an object"""
    attrib = dir(obj)
    return (attrib)
