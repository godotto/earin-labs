from time import sleep
import os

import numpy as np

import optimization_methods as om
import objective_functions as of
import user_input as uin
from stopping_criterion import StoppingMode


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


def select_optimization_method():
    """
    Prompts the user to choose method of optimalization.

    Output:
    function from the optimization_methods module.
    """
    clear_console()
    method = 0
    while method != 1 and method != 2:
        print("Optimization methods:")
        print("1. Gradient descent")
        print("2. Newton's method")
        method = uin.integer_input("Choose method: ")

        if method != 1 and method != 2:
            print("Wrong option")
            sleep(1)
            clear_console()

    return om.gradient_descent if method == 1 else om.newtons_method

def select_objective_function():
    """
    Prompts the user to choose function for optimization.

    Output:
    functions from objective_functions module.
    """
    clear_console()
    function = 0
    while function != 1 and function != 2:
        print("Functions to optimize:")
        print("1. F(x) = ax^3 + bx^2 + cx + d")
        print("2. G(x) = c + b^(T)x + x^(T)Ax")
        function = uin.integer_input("Choose function: ")

        if function != 1 and function != 2:
            print("Wrong option")
            sleep(1)
            clear_console()

    return (of.f_x, of.f_x_gradient) if function == 1 else (of.g_x, of.g_x_gradient)

def select_parameters(objective_function):
    """
    Prompts the user to provide parameters for selected
    objective function.

    Parameters:
    objective_function: handle to one of the objective functions

    Output:
    coefficients: dictionary of coefficients for the selected objective functions.
    """
    clear_console()

    if objective_function == of.f_x:
        coefficients_list = []
        while len(coefficients_list) != 4:
            print("Provide four scalar coefficients (a, b, c, d) for F(x) = ax^3 + bx^2 + cx + d")
            coefficients_list = uin.float_list_input("<separate them with spaces>: ")

            if len(coefficients_list) == 0:
                print("At least one coefficient is wrong")
                sleep(1)
                clear_console()
            elif len(coefficients_list) != 4:
                print("Wrong number of coefficients")
                sleep(1)
                clear_console()
        
        coefficients = {
            'a': coefficients_list[0],
            'b': coefficients_list[1],
            'c': coefficients_list[2],
            'd': coefficients_list[3]
        }
    else:
        d = 0
        while d < 1 or not d:
            print("Provide the dimension d of vector b for G(x) = c + b^(T)x + x^(T)Ax:")
            d = uin.integer_input()

            if d < 1 or not d:
                print("Dimension has to be a positive integer")
                sleep(1)
                clear_console()
        
        clear_console()
        c = 0
        while not c:
            print("Provide the scalar coefficient c for G(x) = c + b^(T)x + x^(T)Ax:")
            c = uin.float_input()

            if not c:
                print("Coefficient has to be a number")
                sleep(1)
                clear_console()

        clear_console()
        b = []
        while len(b) != d:
            print(f"Provide {d} elements of vector b for G(x) = c + b^(T)x + x^(T)Ax")
            b = uin.float_list_input("<separate them with spaces>: ")

            if len(b) == 0:
                print("At least one element is wrong")
                sleep(1)
                clear_console()
            elif len(b) != d:
                print("Wrong number of elements")
                sleep(1)
                clear_console()

        A = []
        A_np = np.array([])

        while not uin.is_positive_definite(A_np):
            while len(A) != d:
                row = []
                while len(row) != d:
                    clear_console()
                    print(f"Provide {d} elements of a row for matrix A for G(x) = c + b^(T)x + x^(T)Ax")
                    row = uin.float_list_input("<separate them with spaces>: ")

                    if len(row) == 0:
                        print("At least one element is wrong")
                        sleep(1)
                        clear_console()
                    elif len(row) != d:
                        print("Wrong number of elements")
                        sleep(1)
                        clear_console()

                A.append(row)
            A_np = np.asarray(A)
            if not uin.is_positive_definite(A_np):
                print("Matrix has to be positive-definite")
                sleep(1)
                clear_console()
                A = []

        coefficients = {
            'A': A_np,
            'b': np.asarray([b]).T,
            'c': c,
            'd': d
        }

    return coefficients

def select_starting_point(objective_function, coefficients):
    """
    Prompts the user to provide starting point for the
    selected method of optimization.

    Parameters:
    objective_function: handle to one of the objective functions
    coefficients: dictionary of coefficients for the selected objective functions

    Output:
    x_0: starting point for the selected method, in form of scalar or vector.
    """
    clear_console()
    method = 0
    while method != 1 and method != 2:
        print("Selection of starting point:")
        print("1. Manual")
        print("2. Random from uniform distribution")
        method = uin.integer_input("Choose method: ")

        if method != 1 and method != 2:
            print("Wrong option")
            sleep(1)
            clear_console()

    if method == 1:
        if objective_function == of.f_x:
            clear_console()
            x_0 = 0
            while not x_0:
                print("Provide a scalar starting point:")
                x_0 = uin.float_input()

                if not x_0:
                    print("Coefficient has to be a number")
                    sleep(1)
                    clear_console()
        else:
            x_0 = []
            while len(x_0) != coefficients['d']:
                print(f"Provide {coefficients['d']} elements of a starting point vector")
                x_0 = uin.float_list_input("<separate them with spaces>: ")

                if len(x_0) == 0:
                    print("At least one element is wrong")
                    sleep(1)
                    clear_console()
                elif len(x_0) != coefficients['d']:
                    print("Wrong number of elements")
                    sleep(1)
                    clear_console()
    else:
        random_range = []
        while len(random_range) != 2:
            print(f"Select range of numbers for uniform distribution (lower first)")
            random_range = uin.int_list_input("<separate them with spaces>: ")

            if len(random_range) == 0:
                print("At least one element is wrong")
                sleep(1)
                clear_console()
            elif len(random_range) != 2:
                print("Wrong number of elements")
                sleep(1)
                clear_console()
            elif random_range[0] >= random_range[1]:
                print("Lower boundary cannot be higher or equal to the higher boundary")
                sleep(1)
                clear_console()
                random_range = []

        if objective_function == of.f_x:
            x_0 = np.random.uniform(random_range[0], random_range[1])
        else:
            x_0 = np.random.uniform(random_range[0], random_range[1], (1, coefficients['d'])).T

    return x_0

def select_stopping_criterion():
    """
    Prompts the user to select one of the three available
    stopping criterions.

    Output:
    enumeration value from StoppingMode enumeration.
    """
    clear_console()
    criterion = 0
    while criterion != 1 and criterion != 2 and criterion != 3:
        print("Stopping criterion:")
        print("1. Maximal number of iterations")
        print("2. Maximal computation time")
        print("3. Compute until desired value is reached")
        criterion = uin.integer_input("Choose method: ")

        if criterion != 1 and criterion != 2 and criterion != 3:
            print("Wrong option")
            sleep(1)
            clear_console()

    return StoppingMode(criterion)

def select_stopping_value(stopping_criterion_mode):
    """
    Prompts the user to provide stopping value
    for the selected stopping criterion.

    Parameters:
    stopping_criterion_mode: enumeration value from StoppingMode enumeration

    Output:
    stopping_value: stopping value for the selected method of stopping.
    """
    stopping_value = 0
    clear_console()
    if stopping_criterion_mode == StoppingMode.MAX_ITERATION:
        while stopping_value < 1 or not stopping_value:
            print("Provide maximal number of algorithm's iteration:")
            stopping_value = uin.integer_input()

            if stopping_value < 1 or not stopping_value:
                print("It has to be a positive integer")
                sleep(1)
                clear_console()
    elif stopping_criterion_mode == StoppingMode.MAX_TIME:
        while stopping_value < 0 or not stopping_value:
            print("Provide maximal time of computation (in seconds):")
            stopping_value = uin.float_input()

            if stopping_value < 0 or not stopping_value:
                print("It has to be a non-negative number")
                sleep(1)
                clear_console()
    else:
        while not stopping_value:
            print("Provide desired value to be reached:")
            stopping_value = uin.float_input()

            if not stopping_value:
                print("It has to be a number")
                sleep(1)
                clear_console()

    return stopping_value

def user_interface():
    optimization_method = select_optimization_method()
    objective_function, gradient = select_objective_function()
    coefficients = select_parameters(objective_function)
    starting_point = select_starting_point(objective_function, coefficients)
    stopping_criterion_mode = select_stopping_criterion()
    stopping_value = select_stopping_value(stopping_criterion_mode)
