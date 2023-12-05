#!/usr/bin/python3

""" The 3-is_kind_of_class module"""


def is_kind_of_class(obj, a_class):

    """is_kind_of_class: returns True if the object is an instance of,
    or inherited from the specified class

    Args:
        obj (object): first parameter
        a_class (class): second parameter

    Return:
        True, otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False
