#!/usr/bin/python3

"""The square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class"""
    def __init__(self, size, x=0, y=0, id=None):
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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ a function to get size"""
        return self.width

    @size.setter
    def size(self, width):
        """a function to set size"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be > 0")
        else:
            self.width = width
            self.height = width

    def update(self, *args, **kwargs):
        """The update to assign variable numbers of attributes"""

        attributes = ["id", "size", "x", "y"]
        for i, arg in enumerate(args):
            setattr(self, attributes[i], arg)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representations"""
        return ({"id": self.id, "size": self.width, "x": self.x, "y": self.y})
