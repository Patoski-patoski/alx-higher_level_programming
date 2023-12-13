#!/usr/bin/python3

"""The 2-rectangle module"""


from models.base import Base


class Rectangle(Base):

    """A Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        """Initialize a Rectangle object
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the top-left corner.
            y (int): The y-coordinate of the top-left corner.
            id (int): The unique identifier for the object. If not provided,
            it will be automatically assigned.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """"a function to get the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """"a function to set the the width"""
        if width <= 0:
            raise ValueError("width must be > 0")
        elif not isinstance(width, int):
            raise TypeError("width must be an integer")
        else:
            self.__width = width

    @property
    def height(self):
        """a function to get the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """"a function to get the height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """"a function to get x"""
        return self.__x

    @x.setter
    def x(self, x):
        """a function to get x"""
        if not isinstance(x, int) and type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """a function to get y"""
        return self.__y

    @y.setter
    def y(self, y):
        """a function to get y"""
        if not isinstance(y, int):
            raise TypeError("x must be an integer")
        if y < 0:
            raise ValueError("x must be >= 0")
        self.__y = y
