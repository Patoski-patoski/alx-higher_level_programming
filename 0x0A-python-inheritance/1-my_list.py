#!/usr/bin/python3

""" The 1-my_list.py module"""


class MyList(list):

    """
    Subclass of the built-in list

    Attributes: In herits all attributes and methods from the
    built-in list clases

    Methods:
        - printed_sorted(): prints the elements in sorted others
    """
    def print_sorted(self):

        """printed_sorted(): prints the elements in sorted others"""
        print(sorted(self))
