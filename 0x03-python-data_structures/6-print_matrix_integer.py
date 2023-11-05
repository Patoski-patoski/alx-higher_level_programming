#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for first in matrix:
        for each in first:
            print("{}".format(each), end=" ")
        print()
