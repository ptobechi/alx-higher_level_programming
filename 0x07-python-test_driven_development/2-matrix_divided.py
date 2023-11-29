#!/usr/bin/python3

"""
A python script that divides element of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides the element of a matrix.

    Parameters:
        matrix (list of lists): Matrix to be divided.
        div (int or float): Divisor.

    Raises:
        TypeError: If the matrix is not a list of lists of int or float,
        or if rows have different sizes. If div is not a number.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list of lists: New matrix with elements divided by div,
        rounded to 2 decimal places.
    """
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return result_matrix
# matrix = [
#    [1, 2, 3],
#    [4, 5, 6]
# ]
# print(matrix_divided(matrix, 3))
# print(matrix)
# print(matrix_divided([[1,2,3],[2,3, 3, 3, "3"]], 5))
