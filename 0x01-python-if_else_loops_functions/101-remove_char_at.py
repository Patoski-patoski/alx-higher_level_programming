#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    tmp = -1
    for i in str:
        tmp += 1
        if tmp == n:
            continue
        new_str += "{}".format(i)
    return new_str
