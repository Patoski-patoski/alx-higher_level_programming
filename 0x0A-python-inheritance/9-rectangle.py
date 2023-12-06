#!/usr/bin/python3

"""The 9-rectangle module"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ derived class Reactangle- a class Rectangle that inherits
    from BaseGeometry
    """

    def __init__(self, width, height):
        """intialize an object instance"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """returns the area of the geometry"""
        return self.__height * self.__width

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
