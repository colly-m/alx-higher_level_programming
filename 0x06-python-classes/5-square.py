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

    def my_print(self):
        """Print square with # character"""
        for i in range(0, self.__size):
            [print("#", end="") for k in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
