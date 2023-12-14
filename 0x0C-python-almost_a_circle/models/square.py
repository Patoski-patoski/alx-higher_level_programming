#!/usr/bin/python3

"""The square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class"""
    "Initialization method
    Args:
        size (int): the size of square
        x (int): the vertical axis
        y (int): the horizontal axis
        id (int): optional
    Return:
        Nothing
     """
        self.width = size
        self.height = size
        super().__init__(size, size, x, y, id)
