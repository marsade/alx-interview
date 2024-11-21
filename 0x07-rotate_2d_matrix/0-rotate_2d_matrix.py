#!/usr/bin/python3
'''Rotate a 2D matrix'''


def rotate_2d_matrix(matrix):
    '''Rotates a 2d matrix in place
    Args: (matrix) - matrix to be rotated
    Returns: (None) - matrix is rotated in place
    '''
    l = len(matrix)
    res = [[0] * l for _ in range(l)]

    for i in range(l):
        for j in range(l):
            res[j][l-1-i] = matrix[i][j]

    for i in range(l):
        for j in range(l):
            matrix[i][j] = res[i][j]
