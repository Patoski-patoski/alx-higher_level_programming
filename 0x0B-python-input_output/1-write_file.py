#!/usr/bin/python3

"""The 1-write_file module"""


def write_file(filename="", text=""):

    """write_file-  reads a text file (UTF8) and prints it to stdout
    Args:
        filename (str): The name of the file to write to.
        text (str):  The text to write to the file.

    Return:
        the lenht of characters written
    """
    def write_file(filename="", text=""):
        with open(filename, "w", encoding="utf-8") as f:
            return f.write(text)
