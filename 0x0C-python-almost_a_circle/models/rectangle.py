#!/usr/bin/python3

"""The 2-rectangle module"""


from models.base import Base


class Rectangle(Base):

    """A Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle object.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the top-left corner.
            y (int): The y-coordinate of the top-left corner.
            id (int): The unique identifier for the object. If not provided,
            it will be automatically assigned.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """"a function to get the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """"a function to set the the width"""
        self.__width = width

    @property
    def height(self):
        """a function to get the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """"a function to get the height"""
        self.__height = height

    @property
    def x(self):
        """"a function to get x"""
        return self.__x

    @x.setter
    def x(self, x):
        """"a function to get x"""
        self.__x = x

    @property
    def y(self):
        """ "a function to get y"""
        return self.__y

    @y.setter
    def y(self, y):
        """"a function to get y"""
        self.__y = y
