#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if 0 <= idx <= len(my_list) -1:
        new_list = my_list[::1]
        new_list[idx] = element
        return new_list
