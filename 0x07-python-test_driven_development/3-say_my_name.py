#!/usr/bin/python3

"""This module demonstrates 3-say_my_name-
   a function that prints My name is <first name> <last name>

   Test file for this module is located in ./tests/ directory
   Run (python3 -m doctest -v ./tests/2-matrix_divided.txt) to test

"""


def say_my_name(first_name, last_name=""):
    """say_my_name- a function that prints first and last name

    Args:
        first_name (str): first parameter
        last_name (str): second parameter

    Return:
        Nothing
    """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    elif type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
