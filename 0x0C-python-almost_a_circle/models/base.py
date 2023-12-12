#!/usr/bin/python3

"""The base module"""


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
