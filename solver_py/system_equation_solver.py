#!/System/Volumes/Data/anaconda3/bin/python

# -*- coding: utf-8 -*-
# @Author: Andres Nowak
# @Date: Tue Feb 25 13:06:15 CST 2020

# This program uses the Gauss-Jordan method

from gauss_jordan import run_through_matrix


def main():
    print("""the equations you write can look like this:\n
			x + 2y + z = 4\n
			3x + z = 2\n
			x-y+z=1\n""")
    size_of_equation = int(input(
        "Of how many unknowns is the system of equations: "))

    matrix_of_equations, list_of_letters_of_unknowns = create_matrix_of_values_of_equations_from_input(
        size_of_equation)

    resolved_matrix = run_through_matrix(matrix_of_equations)

    print_values_of_unknowns(resolved_matrix, list_of_letters_of_unknowns)


def get_equations_from_input(size_of_equation):
    equations = []

    for i in range(size_of_equation):
        equation = input(f"{i + 1} equation: ")

        equations.append(equation)

    return equations


def create_matrix_of_values_of_equations_from_input(size_of_equation):
    matrix_of_equations = []

    equations = get_equations_from_input(size_of_equation)

    list_of_letters_of_unknowns = obtain_unknown_values(equations)
    list_of_letters_of_unknowns = list(list_of_letters_of_unknowns)

    list_of_letters_of_unknowns.sort()

    for equation in equations:
        equation_values = [0] * (len(list_of_letters_of_unknowns) + 1)

        equation_values = get_equation_values(
            list_of_letters_of_unknowns, equation_values, equation)

        matrix_of_equations.append(equation_values)

    print(matrix_of_equations)

    return matrix_of_equations, list_of_letters_of_unknowns


def get_equation_values(list_of_letters_of_unknowns, equation_values, equation):
    signs = set(["+", "-"])

    index = len(list_of_letters_of_unknowns)

    number_value = ""

    if equation[0] not in signs:
        equation = "+" + equation

    for value in equation[::-1]:
        if value.lower() in list_of_letters_of_unknowns:
            index = list_of_letters_of_unknowns.index(value)

            equation_values[index] = 1
        elif value in signs:
            equation_values[index] = float(
                value + number_value[::-1] if number_value else value + str(equation_values[index]))

            number_value = ""
        elif value == "=" and number_value:
            equation_values[index] = float(number_value[::-1])

            number_value = ""
        elif not value.isspace() and value != "=":
            number_value += value

    return equation_values


def obtain_unknown_values(equations):
    unknown_values = set()

    for equation in equations:
        for i in equation:
            if i.isalpha():
                unknown_values.add(i.lower())

    return unknown_values


def print_values_of_unknowns(matrix, list_of_letters_of_unknowns):
    for index, row in enumerate(matrix):
        print(f"{list_of_letters_of_unknowns[index]} = {float(row[-1]):.5f}")


if __name__ == "__main__":
    """matrix = [[1, -6, 3, -2], [2, -3, 1, -2], [3, 3, -2, 2]]
    resolved_matrix = run_through_matrix(matrix)"""

    main()
