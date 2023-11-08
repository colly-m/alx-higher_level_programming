#!/usr/bin/python3
"""Function to get a list of lists of a pascal_traigle module."""


def pascal_triangle(n):
    """Defines a pascal traingle class body."""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tria = triangles[-1]
        temp = [1]
        for t in range(len(tria) - 1):
            temp.append(tria[t] + tria[t + 1])
        temp.append(1)
        triangles.append(temp)
    return
