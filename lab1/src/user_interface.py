from time import sleep
import os

import optimization_methods as om
import objective_functions as of


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
        method = int(input("Choose method: "))

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
        function = int(input("Choose function: "))

        if function != 1 and function != 2:
            print("Wrong option")
            sleep(1)
            clear_console()

    return (of.f_x, of.f_x_gradient) if function == 1 else (of.g_x, of.g_x_gradient)

def select_parameters(objective_function):
    pass

def user_interface():
    optimization_method = select_optimization_method()
    objective_function, gradient = select_objective_function()
