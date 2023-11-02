#!/usr/bin/python3
import sys

if __name__ == "__main__":
    import sys

    len_of_argv = len(sys.argv) - 1
    count = 1

    if len_of_argv == 0:
        print("0 arguments.")
    elif len_of_argv == 1:
        print("{} argument:".format(len_of_argv))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(len_of_argv))
        while count < len_of_argv + 1:
            print("{}: {}".format(count, sys.argv[count]))
            count += 1
