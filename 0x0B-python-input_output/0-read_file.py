#!/usr/bin/python3

"""The 0-read_file module"""


def read_file(filename=""):

    """read_file-  reads a text file (UTF8) and prints it to stdout
    Args:
        filename (str): firs parameter

    Return:
        Nothing
    """
    with open(filename, "r", encoding="UTF8") as f:
       std_out = f.read()
       print(std_out)
