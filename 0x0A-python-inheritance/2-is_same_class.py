#!/usr/bin/python3

""" The 2-is_same_class module"""


def is_same_class(obj, a_class):

    """is_same_class- a function that returns True if the object is exactly an
    instance of the specified class

    Args:
        obj (variable): the object variable
        a_class: the object name

    Return:
        True if exactly an instance, False otherwise
    """
    return type(obj) is a_class
