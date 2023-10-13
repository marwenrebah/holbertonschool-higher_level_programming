#!/usr/bin/python3

"""
Write a function that divides all elements of a matrix.
"""


def divide(new, d):
    """
    Divide all elements in the matrix 'new' by 'd'
    and round the result to 2 decimals.
    """
    for i in range(len(new)):
        new[i] = list(map(lambda x: round(x / 3, 2), new[i]))
    return new


def row_len(matrix):
    """
    Check if each row of the matrix has the same length.

    """
    test = True
    i = 0
    while i < len(matrix) - 1:
        if len(matrix[i]) == len(matrix[i + 1]):
            i += 1
        else:
            test = False
            break
    return test


def matrix_divided(matrix, div):
    """
    Divide all elements of the matrix by 'div'.
    """
    nested_list = any(isinstance(i, list) for i in matrix)
    typeint_list = any(isinstance(i, int) for i in matrix)
    typeflo_list = any(isinstance(i, float) for i in matrix)
    if not nested_list and (not typeint_list or not typeflo_list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    elif not row_len(matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new = divide(matrix.copy(), div)
        return new
