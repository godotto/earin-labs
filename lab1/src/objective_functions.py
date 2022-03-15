import numpy as np

def f_x(x, coefficients):
    """
    Returns value of function F(x)=ax^3+bx^2+cx+d for
    given coefficients and argument.

    Parameters:
    x: argument passed to F(x)
    coefficients: dictionary of function's coefficients.
    """
    return coefficients['a'] * x ** 3 + coefficients['b'] * x ** 2 + coefficients['c'] * x + coefficients['d']


def f_x_gradient(x, coefficients):
    """
    Returns value of function F(x)'s gradient for
    given coefficients and argument.

    Parameters:
    x: argument passed to function's gradient
    coefficients: dictionary of function's coefficients.
    """
    return 3 * coefficients['a'] * x ** 2 + 2 * coefficients['b'] * x + coefficients['c']

def g_x(x, coefficients):
    """
    Returns value of function G(x)=c+b^Tx+x^TAx for
    given coefficients and argument. A has to be
    a positive-definitive matrix. c is a scalar and
    b and x are column vectors.

    Parameters:
    x: argument passed to G(x)
    coefficients: dictionary of function's coefficients.
    """
    return (coefficients['c'] + coefficients['b'].T @ x + x.T @ coefficients['A'] @ x)[0][0]

def g_x_gradient(x, coefficients):
    """
    Returns value of function G(x)'s gradient for
    given coefficients and argument. A has to be
    a positive-definitive matrix. c is a scalar and
    b and x are column vectors.

    Parameters:
    x: argument passed to function's gradient
    coefficients: dictionary of function's coefficients.
    """
    return (coefficients['b'] + coefficients['A'] @ x + coefficients['A'].T @ x)

def f_x_derivative_result(x, coefficients):
    first_derivative_of_x = 3 * coefficients['a'] * x ** 2 + 2 * coefficients['b'] * x + coefficients['c']
    second_derivative_of_x = 6 * coefficients['a'] * x + coefficients['b']

    return first_derivative_of_x/second_derivative_of_x

def g_x_derivative_result (x, coefficients):
    first_derivative_of_x = (coefficients['b'] + 2 * coefficients['A'] @ x)
    second_derivative_of_x = 2 * coefficients['A']

    return first_derivative_of_x/second_derivative_of_x

