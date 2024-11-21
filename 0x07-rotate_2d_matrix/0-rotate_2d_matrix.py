#!/usr/bin/python3
'''Rotate a 2D matrix'''


def rotate_2d_matrix(matrix):
    '''Rotates a 2d matrix in place
    Args: (matrix) - matrix to be rotated
    Returns: (None) - matrix is rotated in place
    '''
    length = len(matrix)
    res = [[0] * length for _ in range(length)]

    for i in range(length):
        for j in range(length):
            res[j][length-1-i] = matrix[i][j]

    for i in range(length):
        for j in range(length):
            matrix[i][j] = res[i][j]
