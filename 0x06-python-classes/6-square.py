#!/usr/bin/python3

''' a class Square that defines a square by: (based on 1-square.py) '''


class Square:

    ''' Square- the class that defines a square'''
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print((" " * self.__position[0] + "#" * self.__size + "\n") * self.__size, end="")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(n, int) and n >= 0 for n in value):
                    raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
