#!/usr/bin/python3
"""Module defines a sqare class that inherits from rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class body"""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """Defines area of square"""
        return (self.__size * self.__size)
