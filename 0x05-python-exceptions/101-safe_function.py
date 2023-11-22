#!/usr/bin/python3

from sys import stderr


def safe_function(func, *a):
    try:
        return func(*a)
    except IndexError:
        print("Exception: list index out of range", file=stderr)
        return None
    except ZeroDivisionError:
        print("Exception: division by zero", file=stderr)
        return None
