#!/usr/bin/python3
"""
method that build Pascal's Triangle with n rows.
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of size n.

    Pascal's triangle starts with a single '1' at the top, and each subsequent
    row is built by adding the two values above each position. The edges of
    the triangle are always '1'.

    Args:
        n: The number of rows to generate in Pascal's triangle.

    Returns:
        A list of lists, where each list represents a row of Pascal's triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        row.append(1)
        triangle.append(row)

    return (triangle)
