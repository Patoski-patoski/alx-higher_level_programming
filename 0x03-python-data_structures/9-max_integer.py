#!/usr/bin/python3

def max_integer(my_list=[]):
    temp = 0

    for list in my_list:
        if not list:
            return None
    for biggest in my_list:
        if biggest > temp:
            temp = biggest
    return temp
