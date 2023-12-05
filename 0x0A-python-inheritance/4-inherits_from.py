#!/usr/bin/python3

""" The 4-inherits_from module"""


def inherits_from(obj, a_class):

    """inherits_from- returns True if the object is an instance of,
    or inherited from the specified class

    Args:
        obj (object): first parameter
        a_class (class): second parameter

    Return:
        True, otherwise False
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
