def f_x(x, coefficients):
    """
    Returns value of function F(x)=ax^3+bx^2+cx+d for
    given coefficients and argument.

    x: argument passed to F(x)
    a, b, c, d: function's coefficients.
    """
    return coefficients['a'] * x ** 3 + coefficients['b'] * x ** 2 + coefficients['c'] * x + coefficients['d']


def f_x_gradient(x, coefficients):
    """
    Returns value of function F(x)'s gradient.

    x: argument passed to function's gradient
    a, b, c: function's coefficients.
    """
    return 3 * coefficients['a'] * x ** 2 + 2 * coefficients['b'] * x + coefficients['c']
