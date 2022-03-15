import numpy as np
import auxiliary_functions as af

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
    if not af.is_positive_definite(coefficients['A']):
        raise ValueError("Given matrix is not positive-definitive")
    
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
    if not af.is_positive_definite(coefficients['A']):
        raise ValueError("Given matrix is not positive-definitive")

    return (coefficients['b'] + coefficients['A'] @ x + coefficients['A'].T @ x)


def f_x_1st_derivative_coefficients (coefficients):
    coefficients=(coefficients['d'], coefficients['c'], coefficients['b'],coefficients['a'])
    return  np.polynomial.polynomial.polyder(coefficients, 1)
   # return der_coefficients[2] * x ** 2 + der_coefficients[1] * x  + der_coefficients[0]

def f_x_2nd_derivative_coefficients (coefficients):
    coefficients=(coefficients['d'], coefficients['c'], coefficients['b'],coefficients['a'])
    return np.polynomial.polynomial.polyder(coefficients, 2)
   # return der_coefficients[1] * x  + der_coefficients[0]


def f_x_derivative_result(x, first_derivative_coefficients, second_derivative_coefficients):
    first_derivative_of_x = first_derivative_coefficients[2] * x ** 2 + first_derivative_coefficients[1] * x  + first_derivative_coefficients[0] 
    second_derivative_of_x = second_derivative_coefficients[1] * x  + second_derivative_coefficients[0]

    return first_derivative_of_x/second_derivative_of_x

