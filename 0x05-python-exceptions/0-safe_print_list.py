#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        new = list(filter(lambda elem: elem <= x, my_list))

    except IndexError:
        print("Unexpected error occured")
    else:
        for num in new:
            print(num, end="")
        print()
        return num
