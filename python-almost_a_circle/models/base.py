#!/usr/bin/python3
"""create a class Base"""
import json


class Base:
    """this the class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize id in case of id is not none otherwise
        we increment nb_objects and assign its value to id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        list = []
        for obj in list_objs:
            list.append(obj.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON
        string representation json_string:"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(size=8)
        elif cls.__name__ == "Rectangle":
            dummy = cls(height=8, width=8)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as f:
                cont = f.read()
                list = cls.from_json_string(cont)
                instan_l = []
                for dict in list:
                    instan = cls.create(**dict)
                    instan_l.append(instan)
                return instan_l
        except FileNotFoundError:
            return []
