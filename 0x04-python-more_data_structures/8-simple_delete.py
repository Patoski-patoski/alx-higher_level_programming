#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    try:
        if type(key) is str:
            a_dictionary.pop(key)
        else:
            return a_dictionary
    except KeyError:
        return a_dictionary

    return a_dictionary
