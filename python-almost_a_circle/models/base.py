#!/usr/bin/python3
"""
Module with a Base class
"""
import json

class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize instance of the Base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Jsonifies a dictionary so it's quite rightly and longer."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
