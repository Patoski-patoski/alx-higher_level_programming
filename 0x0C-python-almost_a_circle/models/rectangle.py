#!/usr/bin/python3

"""The 2-rectangle module"""


from models.base import Base


class Rectangle(Base):

    """A Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width"""
        self.__x = width

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height"""
        self.__x = height

    @propert
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set x"""
        self.__x = x

    @property
    def y(self):
        """ Get y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Set y"""
        self.__y = y
