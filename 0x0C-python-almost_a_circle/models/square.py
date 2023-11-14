#!/usr/bin/python3
"""Module defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Defines a class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Defines the size of square"""
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assignes arguments to attributes based in position"""
        if args:
            for count, attr in enumerate(args):
                if count == 0:
                    self.id = attr
                if count == 1:
                    self.size = attr
                if count == 2:
                    self.x = attr
                if count == 3:
                    self.y = attr
                else:
                    break
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break

    def to_dictionary(self):
        """A dictionary representation of a square"""
        square_dict = {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
        return (square_dict)

    def __str__(self):
        """String representation of a square"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))
