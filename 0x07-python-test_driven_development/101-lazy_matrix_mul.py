#!/usr/bin/python3
"""Function to multiply 2 matrices sing NumpPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Defines multiplication of only two matrices"""
    try:
        result = np.dot(m_a, m_b)
        return result
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
