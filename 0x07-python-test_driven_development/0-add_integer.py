#!/usr/bin/python3
""" This module contains
add_integer - function that adds up two integers.

Test file for this module is located in ./tests/ directory
Run (python3 -m doctest -v ./tests/0-add_integer.txt) to test
"""


def add_integer(a, b=98):
    """ a function that adds 2 integer.

    Args:
        a (int): The first parameter
        b (int): The second parameter (default: 98)

    Returns:
        int : The sum of the a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
