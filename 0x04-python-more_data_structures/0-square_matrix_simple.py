#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res_matrix = [row[:] for row in matrix]
    for idx1, row in enumerate(res_matrix):
        for idx2, clmn in enumerate(res_matrix):
            res_matrix[idx1][idx2] = row[idx2] ** 2

    return (res_matrix)
