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
