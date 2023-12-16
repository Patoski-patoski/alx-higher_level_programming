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
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return []
