#!/usr/bin/python3

"""The square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        if size <= 0:
            raise ValueError("size must > 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        """Initialization method
        Args:
            size (int): the size of square
            x (int): the vertical axis
            y (int): the horizontal axis
            id (int): optional
        Return:
            Nothing
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Test to  overriding the __str__ method"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """ a function to get size"""
        return self.width

    @size.setter
    def size(self, width):
        """a function to set size"""
        if not isinstance(width, int):
            raise TypeError("size must be an integer")
        elif width < 0:
            raise ValueError("size must be >= 0")
        else:
            self.width = width
            self.height = height
