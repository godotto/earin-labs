from time import sleep
import os

import optimization_methods as om


def clear_console():
    """
    Clears console's output.
    """
    clear_command = "clear"

    if os.name == "nt":
        clear_command = "cls"

    os.system(clear_command)


def select_optimization_method():
    """
    Promps the user to choose method of optimalization.

    Output:
    function from the optimization_methods module.
    """
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


def user_interface():
    optimization_method = select_optimization_method()
