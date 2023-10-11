#!/usr/bin/python3
"""Square generation module
"""


class Square:
    """class defined for square generation
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return Square
