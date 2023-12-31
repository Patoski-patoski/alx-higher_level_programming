#!/usr/bin/python3

"""The 11-square module"""


Rectangle = __import__("9-Rectangle").Rectangle



class Square(Rectangle):
    """a derived class Square that inherits Rectangle class"""

    def __init__(self, size):
        super().__init__(width=size, height=size)

    def area(self):
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        return f"[square] {self._Rectangle__width}/{self._Rectangle__height}"
