#!/usr/bin/python3
"""Defines a rectangle based on another"""


class Rectangle:
    """Rectangle class defination."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance in a constructor."""
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns an informal string representation"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_str += str(self.print_symbol)
            rectangle_str += "\n"
        return (rectangle_str[:-1])

    def __repr__(self):
        """Return internal string representation"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Detects when a rectangle instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Gets the width of a Rectangle instance."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of a Rectangle instance."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a Rectangle instance"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of a Rectangle instance"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        area1 = rect_1.area()
        area2 = rect_2.area()

        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return (rect_1)
        if rect_1.area() < rect_2.area():
            return (rect_2)
