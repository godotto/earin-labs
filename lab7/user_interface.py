import re

# probability of cancer
P_CANCER_T = 0.05
P_CANCER_F = 0.95

# Probabilities of TF, TT, FT, FF
P_CANCER_T_TEST_T = 0.9
P_CANCER_T_TEST_F = 0.2
P_CANCER_F_TEST_T = 0.1
P_CANCER_F_TEST_F = 0.8

QUERY_REGEX = "^(P{1})(:{1})((C|TT|TF){1})$"
EVIDENCE_REGEX = "^(((C|T){1})(:{1})((True|False){1}))$|^$"

# check params correctess with regex
def check_parameter(parameter, regex):
    return re.search(pattern=regex, string=parameter)


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
    query = ""
    evidence = ""
    steps_num = 0
    while check_parameter(query, QUERY_REGEX) == None:
        print("Provide query in format: P:C/TT/TF.")
        print("Example: P:TT, for query on probability of true result of test")
        query = input()

    while True:
        print("(optional) Provide evidence in format: C/T:True/False; to skip evidence press enter.")
        print("Example: C:True, for evidence of true result of cancer")
        evidence = input()

        if check_parameter(evidence, EVIDENCE_REGEX) != None:
            break

    steps_num = integer_input("Provide (int) number of steps to be performed. \n")
    
    print(f"Program parameters: \n query: {query} \n evidence: {evidence} \n number of steps : {steps_num}")

    return query, evidence, steps_num

get_program_parameters()