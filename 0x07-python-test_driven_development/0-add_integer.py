#!/usr/bin/python3
""""Defines the addition function"""


def add_integer(a, b=98):
    """Returns addition of integer a and b"""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        """raises TypeError if either a is not integer"""
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        """raises TypeError if either b is not integer"""
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return (a + b)
