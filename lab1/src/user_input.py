import numpy as np

def integer_input(prompt = ""):
    """
    Takes input from stdin and checks if
    it is a proper integer. Returns false
    if it is not.

    Parameters:
    prompt: prompt message for user input.
    """
    try:
        return int(input(prompt))
    except ValueError:
        return False

def float_list_input(prompt = ""):
    """
    Takes input from stdin and checks if
    it is a proper list of floating-point
    numbers. Returns an empty list if it
    is not.

    Parameters:
    prompt: prompt message for user input.
    """
    try:
        return [float(x) for x in input(prompt).split()]
    except ValueError:
        return []

def float_input(prompt = ""):
    """
    Takes input from stdin and checks if
    it is a proper floating-point number. 
    Returns false if it is not.

    Parameters:
    prompt: prompt message for user input.
    """
    try:
        return float(input(prompt))
    except ValueError:
        return False

def int_list_input(prompt = ""):
    """
    Takes input from stdin and checks if
    it is a proper list of integers. Returns 
    an empty list if it is not.

    Parameters:
    prompt: prompt message for user input.
    """
    try:
        return [int(x) for x in input(prompt).split()]
    except ValueError:
        return []

def is_positive_definite(A):
    """
    Checks if given matrix is positive-definite.

    Parameters:
    A: a matrix in form of the Numpy array.
    """
    if not is_symmetric(A):
        return False

    try:
        np.linalg.cholesky(A)
        return True
    except np.linalg.LinAlgError:
        return False


def is_symmetric(A):
    """
    Checks if given matrix is symmetric.

    Parameters:
    A: a matrix in form of the Numpy array.
    """
    if np.array_equal(A, A.T):
        return True
    else:
        return False
