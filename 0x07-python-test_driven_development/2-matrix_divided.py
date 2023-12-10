#!/usr/bin/python3

"""The modul 2-matrix_divided defines func: matrix_divided(matrix, div)"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix:

    Args:
        matrix: matrix of int or floats
        div: int or float

    Returns:
        new matrix
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers\
/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for elements in row:
            if not isinstance(elements, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")

    matrix_res = [[round(elements / div, 2) for elements in row]
                  for row in matrix]
    return matrix_res
