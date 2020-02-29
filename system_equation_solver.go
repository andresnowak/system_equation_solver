package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
	"sync"
)

func main() {
	fmt.Printf("the equations you write should look like this:\n1x + 2y + 1z = 4\n3x + 0y + 1z = 2\n1x + -1y + 1z = 1\n")

	fmt.Printf("Of how many unknowns is the system of equations: ")
	var size_of_equation_string string
	fmt.Scanln(&size_of_equation_string)

	size_of_equation, _ := strconv.ParseInt(size_of_equation_string, 10, 64)

	matrix_of_equations, list_of_letters_of_unknowns := createMatrixOfValuesOfEquationsFromInput(size_of_equation)

	resolved_matrix := runThroughMatrix(matrix_of_equations)

	printValuesOfUnknowns(resolved_matrix, list_of_letters_of_unknowns)
}

func createMatrixOfValuesOfEquationsFromInput(size_of_equation int64) ([][]float64, []string) {
	list_of_letters_of_unknowns := []string{}
	matrix_of_equations := [][]float64{}

	var i int64
	for i = 0; i < size_of_equation; i++ {
		fmt.Printf("%d equation: ", i+1)

		//Todo: Fix problem where input doesnt work with print from another program
		equation_input := bufio.NewReader(os.Stdin)
		equation_string, _ := equation_input.ReadString('\n')

		equation := strings.Split(equation_string, " ")

		equation_values := []float64{}

		for index, value := range equation {
			if index%2 == 0 {
				if index < len(equation)-1 {
					list_of_letters_of_unknowns = append(list_of_letters_of_unknowns, string(value[len(value)-1]))

					value = value[0 : len(value)-1]
					value, _ := strconv.ParseFloat(value, 64)

					equation_values = append(equation_values, float64(value))
				} else {
					value, _ := strconv.ParseFloat(value[0:len(value)-1], 64)

					equation_values = append(equation_values, value)
				}
			}
		}
		matrix_of_equations = append(matrix_of_equations, equation_values)
	}

	return matrix_of_equations, list_of_letters_of_unknowns
}

func printValuesOfUnknowns(matrix [][]float64, list_of_letters_of_unknowns []string) {
	for index, row := range matrix {
		fmt.Printf("%s = %.5f\n", list_of_letters_of_unknowns[index], row[len(row)-1])
	}
}

func runThroughMatrix(matrix [][]float64) [][]float64 {
	matrix_size := len(matrix)
	order_matrix := createMatrixOperationOrder(matrix_size)

	for index_r, row := range order_matrix {
		for _, col := range row {
			if col == index_r {
				convertTo1(matrix[col], matrix[col][index_r])
			} else {
				convertTo0(matrix[col], matrix[row[0]], matrix[col][index_r])
			}
		}
	}

	return matrix
}

func createMatrixOperationOrder(matrix_size int) [][]int {
	order_matrix := [][]int{}

	for i := 0; i < matrix_size; i++ {
		row := []int{}
		for j := 0; j < matrix_size; j++ {
			if j == 0 {
				row = append(row, i)
			}
			if j != i {
				row = append(row, j)
			}
		}
		order_matrix = append(order_matrix, row)
	}
	return order_matrix
}

func convertTo1(row []float64, value float64) {
	inverse_of_value := math.Pow(value, -1)

	for index, i := range row {
		row[index] = i * inverse_of_value
	}
}

func convertTo0(row []float64, row_to_multiply []float64, value float64) {
	value *= -1

	// This is for multithreading
	var wg sync.WaitGroup

	size := len(row)
	wg.Add(size)

	for index := 0; index < size; index++ {
		go func(index int) {
			defer wg.Done()
			row[index] = (row_to_multiply[index] * value) + row[index]
		}(index)
	}

	wg.Wait()
}
