from random import choice


class BayessianNetwork:
    def __init__(self):
        self.__nodes = {
            "test": {"t": 0.95, "f": 0.05},
            "cancer": {"tt": 0.9, "tf": 0.2, "ft": 0.1, "ff": 0.8},
        }

    def mcmc(self, evidence: dict[str, bool], query: list[str], steps: int):

        variables = evidence
        unobserved_variables_names = [node for node in self.__nodes if node not in evidence]

        # uniformly select random values of unobserved variables
        for variable_name in unobserved_variables_names:
            variables[variable_name] = choice([True, False])

        # set the counters for variables of interest
        counters = {}
        for variable_name in query:
            counters[variable_name] = {True: 0, False: 0}

        # random walking
        for _ in range(steps):
            # draw non-observed variable
            selected_variable = choice(unobserved_variables_names)
            # TODO: Random(P(X_i|MarkovBlanket(X_i)))

            # update counters
            for variable_name in query:
                counters[variable_name][variables[variable_name]] += 1

        return self.__normalize_counters(counters)

    def __normalize_counters(self, counters: dict[str, dict[bool, int]]) -> dict[str, dict[bool, float]]:
        normalized_counters = {}

        for variable_name in counters.keys():
            counter_sum = sum(counters[variable_name].values())
            normalized_counters[variable_name] = {}
            normalized_counters[variable_name][True] = counters[variable_name][True] / counter_sum
            normalized_counters[variable_name][False] = counters[variable_name][False] / counter_sum

        return normalized_counters
