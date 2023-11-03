#!/usr/bin/python3
""" Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """inherits of rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """"instantiation"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string info about this square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    # Getter and setter methods for the 'width' and 'height' property
    @property
    def size(self):
        """Size of this square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
