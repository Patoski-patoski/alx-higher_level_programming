#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    new_list = my_list
    for num in new_list:
        print("{:d}".format(num))
