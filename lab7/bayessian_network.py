from random import choice
import numpy as np

class BayessianNetwork:
    def __init__(self):
        # pre-defined probaility distributions
        self.nodes = {
            "cancer": {True: 0.05, False: 0.95},
            "test": {
                True: {True: 0.9, False: 0.1},
                False: {True: 0.2, False: 0.8}
            }
        }

    def mcmc(self, evidence: dict[str, bool], query: list[str], steps: int):
        """
        Returns result of performing Markov chain Monte Carlo algorithm with Gibbs sampling,
        which is the answer to query in form of probabiblity distribution.

        Parameters:
        evidence: provided evidence dictionary
        query: list of queries to be answered
        steps: number of steps to be performed
        """

        variables = evidence
        unobserved_variables_names = [node for node in self.nodes if node not in evidence]

        # uniformly select random values of unobserved variables
        for variable_name in unobserved_variables_names:
            variables[variable_name] = choice([True, False])

        # set the counters for variables of interest
        counters = {}
        for variable_name in query:
            counters[variable_name] = {True: 0, False: 0}

        # random walking
        for _ in range(steps):
            if len(unobserved_variables_names) != 0:
                # draw non-observed variable
                selected_variable = choice(unobserved_variables_names)

                # select new value for the drawed non-observed variable
                variables[selected_variable] = self.__draw_sample(variables, selected_variable)

            # update counters
            for variable_name in query:
                counters[variable_name][variables[variable_name]] += 1

        return self.__normalize_counters(counters)

    def __draw_sample(self, variables: dict[str, bool], selected_variable: str):
        """
        Returns values sampled with Markov Blanket(X) where X is the selected variable.

        Parameters:
        variables: dictionary of all variables.
        """
        probabilities = []
        
        # variant with checking the node without parents
        if selected_variable == "cancer":
            # P(X = x_j | Parents(X)) * P(Z_i | Parents(Z_i))
            for value in [False, True]:
                probability = self.nodes["cancer"][value]
                probability *= self.nodes["test"][value][variables["test"]]
                probabilities.append(probability)

            # α = 1 / (Bel(Cancer = T) + Bel(Cancer = F))
            alpha = 1 / sum(probabilities)
            probabilities = [alpha * p for p in probabilities] # multiply both beliefs by α
        
        # variant with checking the node without children
        else:
            # P(X = x_j | Parents(X))
            probabilities.append(self.nodes["test"][variables["cancer"]][False])
            probabilities.append(1 - probabilities[0]) # probabilities are simple ones, thus they sum up to 1

        # choose new value for the random variable by roulette strategy
        return np.random.choice([False, True], p=probabilities)

    def __normalize_counters(self, counters: dict[str, dict[bool, int]]) -> dict[str, dict[bool, float]]:
        """
        Returns a dictionary of normalized counters.

        Parameters:
        counters: dictionary of value counters
        """
        normalized_counters = {}

        for variable_name in counters.keys():
            counter_sum = sum(counters[variable_name].values())
            normalized_counters[variable_name] = {}
            normalized_counters[variable_name][True] = counters[variable_name][True] / counter_sum      # true_probability = true_count / (true_count + false_count)
            normalized_counters[variable_name][False] = counters[variable_name][False] / counter_sum    # false_probability = false_count / (true_count + false_count)

        return normalized_counters
