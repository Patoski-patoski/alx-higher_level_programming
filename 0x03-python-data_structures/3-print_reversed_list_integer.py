#!/usr/bin/python3
def print_reversed_list_integer(my_list=None):
    if my_list is None:
        my_list = []
    my_list = my_list[::-1]
    for num in my_list:
        print("{:d}".format(num))
