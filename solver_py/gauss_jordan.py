#!/System/Volumes/Data/anaconda3/bin/python

# -*- coding: utf-8 -*-
# @Name: Andres Nowak
# @Date: Sun May 10 16:13:36 CDT 2020

from fractions import Fraction as frac
from sys import exit


def run_through_matrix(matrix):
    """
    It will run through the matrix of values of the system of equations we
    pass it, and get change the values in the matrix with gauss jordan method
    until we run through all the matrix and then return the same matrix solved.
    """

    matrix_size = len(matrix)
    order_matrix = create_matrix_operation_order(matrix_size)

    for index_c, col in enumerate(order_matrix):
        for row in col:
            if row == index_c:
                convert_to_1(matrix[row], matrix[row][index_c])
            else:
                convert_to_0(matrix[row], matrix[col[0]], matrix[row][index_c])

    return matrix


def create_matrix_operation_order(matrix_size):
    order_matrix = []

    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            if j == 0:
                row.append(i)
            if j != i:
                row.append(j)

        order_matrix.append(row)

    return order_matrix


def convert_to_1(row, value):
    try:
        value = frac(value)
        inverse_of_value = value**-1
        for index, i in enumerate(row):
            row[index] = frac(i) * inverse_of_value
    except ZeroDivisionError:
        print("This system of equations cant be solved")
        exit()


def convert_to_0(row, row_to_multiply, value):
    index = 0
    value *= -1

    for i, j in zip(row, row_to_multiply):
        row[index] = (j * value) + i

        index += 1
