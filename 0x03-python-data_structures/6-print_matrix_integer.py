#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for width in range(len(matrix)):
        for num in range(len(matrix[width])):
            print("{:d}".format(matrix[width][num]), end="")
            if num != (len(matrix[width]) - 1):
                print(" ", end="")

        print("")
