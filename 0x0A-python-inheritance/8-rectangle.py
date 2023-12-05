#!/usr/bin/python3

""" The 7-base_geometry module"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ derived class Reactangle- a class Rectangle that inherits
    from BaseGeometry
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
