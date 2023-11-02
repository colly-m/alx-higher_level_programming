#!/usr/bin/python3
"""Function to multiply two matrices"""


def matrix_mul(m_a, m_b):
    """Defines validity of m_a  and m_b"""
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if not m_a or not all(row for row in m_a) or not m_b or not all(row for row in m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    """Checks if elements in the matrices are ints ore floats"""
    if not all(isinstance(element, (int, float)) for row in m_a for element in row) or not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    """Checks if m_a and m_b are rectangular"""
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("Each row of m_a must be of the same size or each row of m_b must be of the same size")

    """Checks if m_a and m_b can be multiplied"""
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can,t be multiplied")

    """perform matrix operation"""
    outcome = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                outcome[i][j] += m_a[i][k] * m_b[k][j]

    return (outcome)
