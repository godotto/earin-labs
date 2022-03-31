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

