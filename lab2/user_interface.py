from time import sleep
import os

import numpy as np
import user_input as uin


def clear_console():
    """
    Clears console's output.
    """
    # if OS is *nix
    clear_command = "clear"

    # if OS is Windows
    if os.name == "nt":
        clear_command = "cls"

    os.system(clear_command)



def select_parameters():
    """
    Prompts the user to provide parameters for the function.

    Parameters:
    -

    Output:
    coefficients: dictionary of coefficients for the function.
    """
    clear_console()

    n = 0
    while n < 1 or not n:
        print("Provide the dimension n of vector b and of matrix A (n x n) for G(x) = c + b^(T)x + x^(T)Ax:")
        n = uin.integer_input()

        if n < 1 or not n:
            print("Dimension has to be a positive integer.")
            sleep(1)
            clear_console()
        
    clear_console()
    c = 0
    while not c:
        print("Provide the scalar coefficient c for G(x) = c + b^(T)x + x^(T)Ax:")
        c = uin.float_input()

        if not c:
            print("Coefficient has to be a number.")
            sleep(1)
            clear_console()

    clear_console()
    b = []
    while len(b) != n:
        print(f"Provide {n} elements of vector b for G(x) = c + b^(T)x + x^(T)Ax:")
        b = uin.float_list_input("<separate them with spaces>: ")

        if len(b) == 0:
            print("At least one element is wrong.")
            sleep(1)
            clear_console()
        elif len(b) != n:
            print("Wrong number of elements.")
            sleep(1)
            clear_console()

    A = []
    A_np = np.array([])

    while not uin.is_positive_definite(A_np):
        while len(A) != n:
            row = []
            while len(row) != n:
                clear_console()
                print(f"Provide {n} elements of a row for matrix A for G(x) = c + b^(T)x + x^(T)Ax:")
                row = uin.float_list_input("<separate them with spaces>: ")

                if len(row) == 0:
                    print("At least one element is wrong.")
                    sleep(1)
                    clear_console()
                elif len(row) != n:
                    print("Wrong number of elements.")
                    sleep(1)
                    clear_console()

            A.append(row)
        A_np = np.asarray(A)
        if not uin.is_positive_definite(A_np):
            print("Matrix has to be positive-definite.")
            sleep(1)
            clear_console()
            A = []

    coefficients = {
        'A': A_np,
        'b': np.asarray([b]).T,
        'c': c,
        'n': n
    }

    return coefficients

def select_range():

    clear_console()

    d = 0
    while d < 1 or not d:
        print("Provide d for the range of searched integers -2^d <= x_i < 2^d, such that d >=1:")
        d = uin.integer_input()

        if d <= 1 or not d:
            print("Dimension has to be an integer greater than 1.")
            sleep(1)
            clear_console()
    return d

# what is the minimal population size?
def select_population_size():

    clear_console()

    population_size = 0
    while population_size < 1 or not population_size:
        print("Provide the population size:")
        population_size = uin.integer_input()

        if population_size <= 1 or not population_size:
            print("Population size has to be an integer greater than 1.")
            sleep(1)
            clear_console()
    return population_size

def select_iteration_number():

    clear_console()

    number_of_iterations = 0
    while number_of_iterations < 1 or not number_of_iterations:
        print("Provide number of algorithm iterations:")
        number_of_iterations = uin.integer_input()

        if number_of_iterations <= 0 or not number_of_iterations:
            print("Number of iterations has to be an integer greater than 0.")
            sleep(1)
            clear_console()
    return number_of_iterations

def select_probabilities():
    
    clear_console()

    crossover_probability = 0
    while crossover_probability >= 1 or not crossover_probability:
        print("Provide crossover probability:")
        crossover_probability = uin.float_input()

        if crossover_probability >= 1 or not crossover_probability:
            print("Crossover probability has to be a fraction - less than 1.")
            sleep(1)
            clear_console()

    mutation_probability = 0
    while mutation_probability >= 1 or not mutation_probability:
        print("Provide mutation probability:")
        mutation_probability = uin.float_input()

        if mutation_probability >= 1 or not mutation_probability:
            print("Crossover probability has to be a fraction - less than 1.")
            sleep(1)
            clear_console()        
    return crossover_probability, mutation_probability

    pass





def user_interface():
    coefficients = select_parameters()
    print("Chosen function coefficients are \n A:", coefficients['A'], "\n", "b:", coefficients['b'], "\n", "c:", coefficients['c'], "\n" ,"(dimensions) n:", coefficients['n'] )
    d = select_range()
    print(f"Chosen d for x range is: {d}")
    population_size = select_population_size()
    print(f"Chosen population size: {population_size}")
    (crossover_probability, mutation_probability) = select_probabilities() 
    print(f"Chosen crossover probability: {crossover_probability} \n Chosen mutation probability: {mutation_probability} ")
    iteration_number = select_iteration_number()
    print(f"Chosen iteration number: {iteration_number}")