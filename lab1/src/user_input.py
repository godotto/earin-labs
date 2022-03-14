def integer_input(prompt):
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
