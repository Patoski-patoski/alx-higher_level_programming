#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        for list in lists:
            print("{}".format(list), end=" ")
        print()
