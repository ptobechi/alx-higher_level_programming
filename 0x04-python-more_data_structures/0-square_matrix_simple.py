#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions as the input matrix
    result_matrix = [row[:] for row in matrix]

    # Iterate through the rows and columns of the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Compute the square of each element and store it in the result matrix
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix
