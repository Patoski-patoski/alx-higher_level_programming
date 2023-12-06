#!/usr/bin/python3

"""The 8-base_geometry module"""


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

    def __str__(self):
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height)

    def area(self):
        return "{}".format(self.__height * self.__width)

