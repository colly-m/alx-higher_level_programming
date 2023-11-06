#!/usr/bin/python3
"""Module to write a class rectangle inheriting from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class rectangle body """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Defines the area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
