#!/System/Volumes/Data/anaconda3/bin/python

# -*- coding: utf-8 -*-
# @Author: Andres Nowak
# @Date: Tue Feb 25 13:06:15 CST 2020

# This program uses the Gauss-Jordan method

from fractions import Fraction as frac


def main():
    print("""the equations you write should look like this:\n
            1x + 2y + 1z = 4\n
            3x + 0y + 1z = 2\n
            1x + -1y + 1z = 1\n""")
    size_of_equation = int(input(
        "Of how many unknowns is the system of equations: "))

    matrix_of_equations, list_of_letters_of_unknowns = create_matrix_of_values_of_equations_from_input(
        size_of_equation)

    resolved_matrix = run_through_matrix(matrix_of_equations)

    print_values_of_unknowns(resolved_matrix, list_of_letters_of_unknowns)


def create_matrix_of_values_of_equations_from_input(size_of_equation):
    list_of_letters_of_unknowns = []
    matrix_of_equations = []

    for i in range(size_of_equation):
        equation = input(f"{i + 1} equation: ")
        equation = equation.split()

        equation_values = []

        for index, value in enumerate(equation):
            if index % 2 == 0:
                if index != len(equation) - 1:
                    equation_values.append(float(value[0:-1]))

                    list_of_letters_of_unknowns.append(value[-1])
                else:
                    equation_values.append(float(value))

        matrix_of_equations.append(equation_values)

    return matrix_of_equations, list_of_letters_of_unknowns


def print_values_of_unknowns(matrix, list_of_letters_of_unknowns):
    for index, row in enumerate(matrix):
        print(f"{list_of_letters_of_unknowns[index]} = {row[-1]}")


def run_through_matrix(matrix):
    matrxix_size = len(matrix)
    order_matrix = create_matrix_operation_order(matrxix_size)

    count = 0

    for index_r, row in enumerate(order_matrix):
        for col in row:
            if col == index_r:
                convert_to_1(matrix[col], matrix[col][index_r])
            else:
                convert_to_0(matrix[col], matrix[row[0]], matrix[col][index_r])

    return matrix


def create_matrix_operation_order(matrix_size):
    order_matrix = []

    for i in range(matrix_size):
        row = []
        for index, j in enumerate(range(matrix_size)):
            if index == 0:
                row.append(i)
            if index != i:
                row.append(j)

        order_matrix.append(row)

    return order_matrix


def convert_to_1(row, value):
    value = frac(value)
    inverse_of_value = value**-1
    for index, i in enumerate(row):
        row[index] = frac(i) * inverse_of_value


def convert_to_0(row, row_to_multiply, value):
    index = 0
    value *= -1

    for i, j in zip(row, row_to_multiply):
        row[index] = (j * value) + i

        index += 1


if __name__ == "__main__":
    """matrix = [[1, -6, 3, -2], [2, -3, 1, -2], [3, 3, -2, 2]]
    resolved_matrix = run_through_matrix(matrix)"""

    main()
