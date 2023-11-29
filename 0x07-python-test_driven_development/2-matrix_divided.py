#!/usr/bin/python3

"""
A python script that divides element of a matrix
"""

def matrix_divided(matrix, div):
    """
    divides the element of a matrix
    Parameters:
        matrix (list (int, float): matrix must be a list of int or float
    Raises:
        TypeError: if the matrix list is not a list of int or float and same
        size in rows
        ZeroDivisionError: on every devision by zero
    Returns:
        A new matrix
    """
    for element in matrix:
        if not isinstance(element, (int, float)):
            raise TypeError("matrix must be a matrix (list of 
                    lists)of integers/floats")

    if all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    result_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return result_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
