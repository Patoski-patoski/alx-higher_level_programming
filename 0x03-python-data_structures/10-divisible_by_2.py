#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    for item in my_list:
        if item % 2:
            new_list.append(False)
        else:
            new_list.append(True)

    return new_list
