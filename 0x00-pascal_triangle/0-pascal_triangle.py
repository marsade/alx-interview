#!/usr/bin/python3
'''
Returns a list of lists of integers representing the Pascal’s triangle of n
'''


def pascal_triangle(n):
    '''Returns a lists of lists of pascals triangle'''

    ml = []
    if n <= 0:
        return []
    else:
        for i in range(1, n+1):
            pt = []
            C = 1
            for j in range(1, i + 1):
                pt.append(C)
                C = C * (i - j) // j
            ml.append(pt)
        return ml
