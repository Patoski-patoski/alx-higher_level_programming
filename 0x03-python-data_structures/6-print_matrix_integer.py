#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for list in lists:
            print("{:d}".format(list), end=" ")
        print()
