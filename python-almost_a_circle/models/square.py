#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this is the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """use all attributes of Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """[Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """retrieve  the value of size"""
        return self.width

    @size.setter
    def size(self, size):
        """assign size to width and height"""
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """assign argument to each attribute"""
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """return the dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
