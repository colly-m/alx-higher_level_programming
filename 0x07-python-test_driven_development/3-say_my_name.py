#!/usr/bin/python3
"""Function to print my first and last name"""


def say_my_name(first_name, last_name=""):
    """Check if name  given is string"""
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string")
    
    full_name = first_name + " " + last_name
    print("My name is " + full_name)
