#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    if value == None:
        return False
    try:
        print("{:d}".format(value))
        return value
    except (TypeError, NameError, ValueError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    else:
        return False
