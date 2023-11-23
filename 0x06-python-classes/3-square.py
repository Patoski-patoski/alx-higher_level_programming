#!/usr/bin/python3

""" a class Square that defines a square by: (based on 1-square.py)"""


class Square:

    """Square- the class that defines a square"""
    def __init__(self, size=0):
        """__init__"- (method) initialize attributes(arguments) of an object

        Args:
                self: a reference to an instance of the class
                size: size of the square

        Return:
                None
         """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area: that returns the current square area"""

        return self.__size * self.__size
