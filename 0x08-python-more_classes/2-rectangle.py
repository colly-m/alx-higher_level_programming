#!/usr/bin/python3
"""Defines triangle area and perimeter"""


class Rectangle:
    """Defines a class rectangle"""
    def __init__(self, width=0, height=0):
        """Initialises the features of the object"""
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of a rectangle instance"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        sets the width of a rectangle
        value: value of the width, must be a positive int
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the width of a rectangle instance"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        sets the height of a rectangle
        value: value of the height, must be a positive int
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Defines the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Defines the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))
