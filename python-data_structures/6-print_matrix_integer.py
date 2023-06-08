#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        if not row:
            print("")
        else:
            print(''.join(str(element) for element in row))
