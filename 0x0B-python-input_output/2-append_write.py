#!/usr/bin/python3

"""The 2-append_write module"""


def append_write(filename="", text=""):

    """write_file-  appends a string at the end of a text file (UTF8)
    Args:
        filename (str): The name of the file to write to.
        text (str):  The text to write to the file.

    Return:
         returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
