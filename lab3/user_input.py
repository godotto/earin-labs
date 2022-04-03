from numpy import char


def char_input(prompt = ""):
    """
    Takes input from stdin and checks if
    it is a proper floating-point number. 
    Returns false if it is not.

    Parameters:
    prompt: prompt message for user input.
    """
    try:
        return input(prompt)
    except ValueError:
        return False

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

