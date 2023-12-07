#!/usr/bin/python3

"""The 10-square module"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """a derived class Square that inherits Rectangle class"""

    def __init__(self, size):
        super().__init__(width=size, height=size)

    def area(self):
        return self._Rectangle__width * self._Rectangle__height
