#!/usr/bin/python3
"""Defines a square based on another"""


class Square:
    """Square class body"""
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    @property
    def size(self):
        """returns size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of the square."""
        return (self.__size * self.__size)

    def __le__(self, other):
        """
        Compares areas of two squares if one is less than or equal
        to the area of the other.
        Returns:
            bool: True if lessor equal, False otherwise
        """
        return self.area() <= other.area()

    def __lt__(self, other):
        """"
        Compares areas of two squares if this is less than the area
        of the other.
        Returns:
            bool: True if square's area is less, False if otherwise
        """
        return self.area() < other.area()

    def __ge__(self, other):
        """"
        Compares areas of two squares if this is greater than or equal
        to the area of the other.
        Returns:
            bool: True if square's area is greater than or equal to the other
            , False if otherwise
        """
        return self.area() >= other.area()

    def __ne__(self, other):
        """"
        Compares areas of two squares if they are different
        Returns:
            bool: True if squares are different, False if otherwise
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """"
        Compares areas of two squares if this is less greater the area
        of the other.
        Returns:
            bool: True if square's area is greater, False if otherwise
        """
        return self.area() > other.area()

    def __eq__(self, other):
        """"
        Compares areas of two squares if this is equal to the area
        of the other.
        Returns:
            bool: True if square's area is equal, False if otherwise
        """
        return self.area() == other.area()
