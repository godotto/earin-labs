import numpy as np


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
