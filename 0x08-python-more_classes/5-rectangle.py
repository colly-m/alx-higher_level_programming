#!/usr/bin/python3
"""Defines a rectangle based on another"""


class Rectangle:
    """Defines a class rectangle"""
    def __init__(self, width=0, height=0):
        """Initialises the features of the object"""
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

    def __str__(self):
        """Returns an informal string representation"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_str = ""
        for a in range(self.__height):
            for b in range(self.__width):
                rectangle_str += "#"
            rectangle_str += "\n"
        return (rectangle_str[:-1])

    def __repr__(self):
        """Returns a formal string representation of a rectangle"""
        return (f'Rectangle({self.__width}, {self.__height})')

    def __del__(self):
        """Defines an instance being deleted"""
        print("Bye rectangle...")

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
