#!/usr/bin/python3
"""define a function"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tris = triangle[-1]
        row = [1]
        for idx in range(len(tris) - 1):
            row.append(tris[idx] + tris[idx + 1])
        row.append(1)
        triangle.append(row)
    return triangle
