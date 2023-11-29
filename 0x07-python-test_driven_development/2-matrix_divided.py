#!/usr/bin/python3

"""This module demonstrates
2-matrix_divided- a matrix module to be divide

Test file for this module is located in ./tests/ directory
Run (python3 -m doctest -v ./tests/2-matrix_divided.txt) to test
"""


def check_size(matrix):

    """check_size- a function to check the size of a matrix

    Args:
        matrix (int or floats): list of list

    Return:
        bool: True if equal size, False otherwise
    """

    if not matrix:
        return True
    row_size = len(matrix[0])
    return all(len(row) == row_size for row in matrix)


def matrix_divided(matrix, div):
    """matrix_divided- a function that divides all elements of a matrix

    Args:
        matrix (int or floats): The first parameter
        div (int or floats): The second parameter

    Returns:
        list of list: A new matrix
    """

    new_matrix = []
    for outer in matrix:
        a_matrix = []
        for inner in outer:
            if type(inner) not in [int, float]:
                raise TypeError(
                   "matrix must be a matrix (list of lists) of integers/floats"
                        )
            elif not check_size(matrix):
                raise TypeError(
                    "Each row of the matrix must have the same size"
                 )
            elif type(div) not in [int, float]:
                raise TypeError("div must be a number")
            elif div == 0:
                raise ZeroDivisionError("division by zero")
            else:
                inner = inner / div
                a_matrix.append(round(inner, 2))
        new_matrix.append(a_matrix)
    return new_matrix
