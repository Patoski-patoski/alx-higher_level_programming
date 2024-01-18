#!/usr/bin/python3

"""The base module"""

import json


class Base:
    """ A base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Rectangle object

        Args:
            id (int): The unique identifier for the object.
            If not provided  it will be automatically assigned
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """To return the JSON string representation of list_dictionaries"""
        if list_dictionaries is not None or list_dictionaries is []:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, lists_objs):
        """Saves a list of instances to a JSON file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            if lists_objs is None:
                file.write("[]")
            else:
                lists_dicts = [obj.to_dictionary() for obj in lists_objs]
                json_str = cls.to_json_string(lists_dicts)
                file.write(json_str)
