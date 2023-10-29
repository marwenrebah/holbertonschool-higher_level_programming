#!/usr/bin/python3
"""
Module with a Base class
"""


class Base:
    """Class Base"""
    __nb_objects = 0


def __init__(self, id=None):
    """Initializes instances of the Base class"""
    if id is None:
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
    else:
        self.id = id
