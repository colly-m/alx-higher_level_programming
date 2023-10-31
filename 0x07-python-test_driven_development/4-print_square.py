#!/usr/bin/python3
"""Function to print a square with a character #"""


def print_square(size):
    """Defines a square printed with #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
