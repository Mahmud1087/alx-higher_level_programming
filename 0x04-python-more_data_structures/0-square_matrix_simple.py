#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newList = []
    for x in matrix:
        newList.append([y**2 for y in x])
    return newList
