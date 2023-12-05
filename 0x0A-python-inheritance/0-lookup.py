#!/usr/bin/python3

"""The 0-lookup module"""


def lookup(obj):
    """  Returns a list of attributes and methods of the provided object.

    Args:
         obj (object): The object for which attributes and methods
         will be looked up.

    Returns:
        list: A list containing the names of attributes and
        methods of the object.

    """
    if not isinstance(obj, object):
        raise TypeError("Input Value must be an object")

    return list(dir(obj))
