#!/usr/bin/python3
import math
"""Defines operations on a circle"""


class MagicClass:
    """A class to compute area and circumference of a acircle"""
    def __init__(self, radius):
        """
        Initializes the MagicClass with a given radius
        Arguments of the raduis should be float
        TypeError if radius is not number
        """
        if not (isisnstance(radius, int) or isinstance(radius, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates and returns the area"""
        return (math.pi * (self.__radius ** 2)

    def circumference(self):
        """Calculates and returns the circumference"""
        return (2 * math.pi * self.__radius)
