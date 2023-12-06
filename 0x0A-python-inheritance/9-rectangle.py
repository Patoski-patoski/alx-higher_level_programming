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

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return f"[{Rectangle.__name__}] {self.__width}/{self.__height}"


class Square(Rectangle):

    def __init__(self, size):
        super()._init__(width=size, height=size)

    def area(self):
        return self.__width * self.__height
