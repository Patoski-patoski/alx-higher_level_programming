#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return value
    except TypeError as err:
        print(err, file=sys.stderr)
        return False
