import stopping_criterion as sc
import objective_functions as of

def gradient_descent(starting_point, objective_function, coefficients, gradient, step_size, stopping_criterion_mode, stopping_criterion_value):
    """
    Returns solution x and value at this point found by
    gradient descent method.

    Parameters:
    starting_point: x_0, point from which algorithm starts to operate
    objective_function: function that is being analysed
    coefficients: objective function coefficients
    gradient: gradient of analyzed function
    step_size: value by which antigradient is being scaled when new point is calculated
    stopping_criterion_mode: stopping mode given as StoppingMode enum
    stopping_criterion_value: depending on a stopping criterion it might be maximal number
                              of iterations, maximal time spent on calculations or desired
                              value that has to be achieved or exceeded.
    """

    x = starting_point
    stopping_criterion = sc.StoppingCriterion(stopping_criterion_mode, stopping_criterion_value)
    current_value = objective_function(x, coefficients)

    while not stopping_criterion.stopping_criterion(current_value):
        x = x - step_size * gradient(x, coefficients)
        current_value = objective_function(x, coefficients)

    return x, current_value

def newtons_method(starting_point, objective_function, coefficients, derivative_result, stopping_criterion_mode, stopping_criterion_value):
    """
    Returns solution x and value at this point found by
    Newton's method.

    Parameters:
    starting_point: x_0, point from which algorithm starts to operate
    objective_function: function that is being analysed
    coefficients: objective function coefficients
    derivative_result: first derivative of analysed function of x over second derivative of analysed function of x
    stopping_criterion_mode: stopping mode given as StoppingMode enum
    stopping_criterion_value: depending on a stopping criterion it might be maximal number
                              of iterations, maximal time spent on calculations or desired
                              value that has to be achieved or exceeded.
    """
    x = starting_point
    stopping_criterion = sc.StoppingCriterion(stopping_criterion_mode, stopping_criterion_value)
    current_value = objective_function(x, coefficients)

    while not stopping_criterion.stopping_criterion(current_value):
      
       x = x - derivative_result(x, coefficients) # x = x - f'(x)/f"(x)
       current_value = objective_function(x, coefficients)
  
    return  x, current_value

