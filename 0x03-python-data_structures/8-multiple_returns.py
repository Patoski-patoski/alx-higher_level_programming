#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if sentence == "":
        f_char = None
    else:
        f_char = sentence[0]
    return length, f_char
