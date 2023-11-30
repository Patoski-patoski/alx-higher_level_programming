#!/usr/bin/python3


"""
0-rectangle module - contains Rectangle() class
"""


class Rectangle:

    """ A class representing a rectangle.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Attributes:
        __width (int): The width of the rectangle
        __height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):

        """ Initializer for the Rectangle class.

        Args:
            width (int): The width of the rectangle (default: 0).
            height (int): The heigth of the rectangle (default: 0).
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle

        Args:
            value (int): The new value of the width

        Raises:
            ValueError: If the width is less than 0
            TypeError: If the width is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle

        Returns:
            int: the height of the triangle
        """
        return self.__height

    @height.setter
    def height(self, value):

        """Set the height of the rectangle
         Args:
            value (int): the new value of the rectangle

         Raises:
            TypeError: If the height is not an integer
            ValueError: If the height is less than 0
         """
        if not isinstance(value, int):
            raise TypeError(" height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
