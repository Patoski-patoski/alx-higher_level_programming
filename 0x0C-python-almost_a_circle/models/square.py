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

    def validate_size(self):
        """Validate that size is equal to width and height"""
        if self.width != self.height:
            raise ValueError("Size must be equal to both width and \
                             height in a Square")

    def update(self, *args, **kwargs):
        """Update attributes with validation"""
        super().update(*args, **kwargs)
        self.validate_size()

    def __str__(self):
        """Test to  overriding the __str__ method"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
