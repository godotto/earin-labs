import re

QUERY_REGEX  = "^((test|cancer)( )*){1,2}$"
EVIDENCE_REGEX = "^((test|cancer)(:)(True|False)( )*){0,2}$"


def check_query_parameter(parameter, regex):
    """
    Returns query mapped onto a list if it matches provided regex pattern.
    Otherwise returns None value.

    Parameters:
    parameter: query to be checked
    regex: query regex pattern
    """
    query_params = ""
    if re.search(pattern=regex, string=parameter):
       
        query_params =  parameter.split(sep =' ')
        
        return query_params
    
    return None

def check_evidence_parameter(parameter, regex):
    """
    Returns evidence mapped onto a dictionary if it matches provided regex pattern.
    Otherwise returns None value. Empty evidence is allowed.

    Parameters:
    parameter: evidence to be checked
    regex: evidence regex pattern
    """

    if re.search(pattern=regex, string=parameter):
        dictionary = {}

        if parameter.isspace() == False and len(parameter) > 0:

            str_dictionary_elements = parameter.split(sep =' ')

            for el in str_dictionary_elements:
                key, value_str = el.split(sep=':')
                value = False if value_str == "False" else True
                dictionary[key] = value

        return dictionary
    
    return None


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

def get_program_parameters():
    """
    Returns program parameters: query, evidence, number of steps, 
    provided by the user and validated.

    Parameters:
    -
    """

    while True:
        print("(required) Provide query in the following format for each query subject: query_subject, seperated by space.")
        print("Example: cancer, for query on probability of cancer.")
        query_input = input()

        result = check_query_parameter(parameter=query_input, regex=QUERY_REGEX )
        if result != None:
            query_list = result
            break

    while True:
        print("(optional) Provide evidence in the following format for each evidence element: test:False, seperated by space.")
        print("Example: cancer:True for evidence of true result of cancer.")
        evidence_input = input()

        result = check_evidence_parameter(parameter=evidence_input, regex=EVIDENCE_REGEX )
        if result != None:
            evidence_dict = result
            break

    steps_num = integer_input("(required) Provide number of steps to be performed. \n")
    
    print(f"Program parameters: \n query: {query_list} \n evidence: {evidence_dict} \n number of steps: {steps_num}")

    return query_list, evidence_dict, steps_num
