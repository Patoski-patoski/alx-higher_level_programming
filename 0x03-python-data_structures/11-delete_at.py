#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if 0 <= idx <= len(my_list) - 1:
        try:
            del my_list[idx]
        except ValueError:
            return my_list
    return my_list
