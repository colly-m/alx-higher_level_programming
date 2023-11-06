#!/usr/bin/python3
"""Module defines a rectangle of a square subclass"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square class body within a rectangle"""

    def __init__(self, size):

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
