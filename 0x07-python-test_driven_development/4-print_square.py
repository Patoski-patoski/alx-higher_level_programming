#!/usr/bin/python3

"""This module 4-print_square demonstrates
     a function that prints a square with the character #

Test file for this module is located in ./tests/ directory
Run (python3 -m doctest -v ./tests/4-print_square.txt) to test

"""


def print_square(size):

    """print_square- a function that prints a square with the character #
    Args:
        size (int)- first parameter

    Returns:
        Nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        i = size
        while i > 0:
            for j in range(size):
                print("#", end="")
            print()
            i -= 1
