def f_x(x:float, a:float, b:float, c:float, d:float) -> float:
    """
    Returns value of function F(x)=ax^3+bx^2+cx+d for
    given coefficients and argument.

    x: argument passed to F(x)
    a, b, c, d: function's coefficients.
    """
    return a * x ** 3 + b * x ** 2 + c * x + d

def f_x_gradient(x:float, a:float, b:float, c:float) -> float:
    """
    Returns value of function F(x)'s gradient.

    x: argument passed to function's gradient
    a, b, c: function's coefficients.
    """
    return 3 * a * x ** 2 + 2 * b * x + c
