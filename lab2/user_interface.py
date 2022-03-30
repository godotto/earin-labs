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

def user_interface():
    coefficients = select_parameters()
    
