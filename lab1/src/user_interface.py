from time import sleep
import os

import numpy as np

import optimization_methods as om
import objective_functions as of
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


def select_optimization_method():
    """
    Promps the user to choose method of optimalization.

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
    Promps the user to choose function for optimization.

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
    Promps the user to provide parameters for selected
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

        coefficients = {
            'A': np.asarray(A),
            'b': np.asarray([b]).T,
            'c': c
        }

    return coefficients


def user_interface():
    optimization_method = select_optimization_method()
    objective_function, gradient = select_objective_function()
    coefficients = select_parameters(objective_function)
    # TODO: starting point definition and stopping criterion selection
