#!/usr/bin/python3

def max_integer(my_list=[]):
    temp = 0
    if not list:
        return None
    for biggest in my_list:
        if biggest > temp:
            temp = biggest
    return temp
