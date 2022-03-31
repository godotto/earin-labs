import random
import numpy as np

def create_population(size:int, n:int, d:int):
    population = np.ndarray((size, n, 1), dtype=int)

    for i in range(size):
        for j in range(n):
            population[i][j] = random.randrange(-2 ** d, 2 ** d - 1)

    return population

def genome(fenotype:int, d:int):
    binary_string = np.binary_repr(fenotype, d + 1)
    return np.array(list(binary_string), dtype=int)

def fitness_function(x, coefficients):
    return (coefficients['c'] + coefficients['b'].T @ x + x.T @ coefficients['A'] @ x)[0][0]

def scaled_fitness_scores(population, coefficients):
    fitness_scores = []
    for specimen in population:
        fitness_scores.append(fitness_function(specimen, coefficients))

    min_score = min(fitness_scores)
    max_score = max(fitness_scores)

    scaled_fitness_scores = []
    for score in fitness_scores:
        scaled_fitness_scores.append((score - min_score) / (max_score - min_score))

    return scaled_fitness_scores

def roulette_wheel_selection(population, coefficients, number_for_reproduction):
    probabilities = []
    fitness_scores = scaled_fitness_scores(population, coefficients)
    sum_of_scores = sum(fitness_scores)

    for score in fitness_scores:
        probabilities.append(score / sum_of_scores)

    selected_indices = []

    for i in range(number_for_reproduction):
        random_number = random.random()
        sum_of_probabilities = 0

        for j, probability in enumerate(probabilities):
            sum_of_probabilities += probability
            if random_number < sum_of_probabilities:
                selected_indices.append(j)
                break

    return [population[i] for i in selected_indices]
        
