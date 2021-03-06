import random
from unittest import result
import numpy as np

def create_population(size:int, n:int, d:int):
    population = np.ndarray((size, n, 1), dtype=int)

    for i in range(size):
        for j in range(n):
            population[i][j] = random.randint(-2 ** d, 2 ** d - 1)
 
    return population

def to_genome(fenotype:int, d:int):
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
        
def to_fenotype(genome, d:int):
    binary_string = ''.join(str(bit) for bit in genome)
    intermediate_form = int(binary_string, 2)

    if binary_string[0] == '0':
        return intermediate_form
    else:
        return (-1) * (2 ** (d + 1) - intermediate_form)

def crossover(first_parent, second_parent, probability, d, n):
    if random.random() > probability:
        return (first_parent, second_parent)
    
    first_offspring = np.ndarray(shape=(n, 1), dtype=int)
    second_offspring = np.ndarray(shape=(n, 1), dtype=int)
    crossover_point = random.randint(1, d)

    for i in range(n):
        first_parent_genome = to_genome(first_parent[i][0], d)
        second_parent_genome = to_genome(second_parent[i][0], d)

        first_offspring_genome = np.concatenate((first_parent_genome[:crossover_point], second_parent_genome[crossover_point:]), axis=None)
        second_offspring_genome = np.concatenate((second_parent_genome[:crossover_point], first_parent_genome[crossover_point:]), axis=None)

        first_offspring[i] = to_fenotype(first_offspring_genome, d)
        second_offspring[i] = to_fenotype(second_offspring_genome, d)

    return (first_offspring, second_offspring)

def mutation(individual, probability,d):
    for i,fenotype in enumerate(individual):
        genome = to_genome(fenotype[0],d)
        for j,gene in enumerate(genome):
            if random.random() <= probability:
                genome[j] = int(not(gene))
        individual[i] = to_fenotype(genome,d)    
    return individual

def replace(population,offspring_list, number_to_replace):
    for i in range(number_to_replace):
        population = np.delete(population,0,axis=0)
    population = np.append(population,offspring_list,axis=0)  
    return population 

def genetic_algorithm(population, coefficients, n, d, crossover_probability,mutation_probability, number_of_ind_to_replace):

    selected_for_reproduction = roulette_wheel_selection(population,coefficients,number_of_ind_to_replace)
    offspring_list = np.ndarray((number_of_ind_to_replace, n, 1), dtype=int)
    i=0
    while i < len(selected_for_reproduction) - 1:
        (offspring1, offspring2) = crossover(selected_for_reproduction[i], selected_for_reproduction[i+1],crossover_probability,d,n)

        #mutate new individuals
        offspring1 = mutation(offspring1,mutation_probability,d)
        offspring2 = mutation(offspring2,mutation_probability,d)
        
        offspring_list[i] = offspring1
        offspring_list[i + 1] = offspring2
        i+=1

    new_population = replace(population,offspring_list, number_of_ind_to_replace)

    return new_population

def get_algorithm_results(population, coefficients):
    results = []
    for i,specimen in enumerate(population):
        result = (specimen,(fitness_function(specimen,coefficients)))
        print(f"{i+1}. x, f(x): {result} \n")  
        results.append(result)
    return results

def print_results(population_results):
    for result in population_results:
        print(f"x, f(x): {result} \n")         
