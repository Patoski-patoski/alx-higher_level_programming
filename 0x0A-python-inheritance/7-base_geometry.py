#!/usr/bin/python3

""" The 7-base_geometry module"""


class BaseGeometry:

    """ class BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """integer_validator- to validate an object for integer

        Args:
            name (str): firs parameter
            value (int): Second parameter

        Returns:
            Nothing
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
