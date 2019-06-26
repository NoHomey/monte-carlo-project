import random
from typing import List

from genetic_operations import GeneticOperations


def main_algorithm(min_population: int, max_population: int, num_iterations: int, start_tolerance: float,
                   genetic_operations: GeneticOperations, mutation_probability: float, selection_probability: float):

    assert min_population <= max_population

    decreasing_step_tolerance = start_tolerance / num_iterations

    current_tolerance = start_tolerance

    population: List = generate_population(genetic_operations, min_population)

    for iteration in range(num_iterations):
        mutate_population(genetic_operations, population, mutation_probability)
        next_generation = generate_population(genetic_operations, min_population)
        population.extend(next_generation)
        population = select_individuals(population, min_population, max_population, selection_probability)

    return population

def generate_population(genetic_operations: GeneticOperations, size: int) -> List:

    population: List = [genetic_operations.generate() for _ in range(size)]

    return population


def mutate_population(genetic_operations: GeneticOperations, population: List, probability: float) -> List:
    
    count = len(population)

    values_count = genetic_operations.generators_len

    for i in range(count):
        if random.random() < probability:
            mutation_probability = random.random()
            step = 1 / values_count
            current = step
            for j in range(values_count):
                if mutation_probability < current:
                    population.append(genetic_operations.mutate(population[i].values, j))
                    break
                current += step
    
    return population


def select_individuals(population: List, number_of_individuals: int,  max_pupulation: int, probability: float) -> List:

    assert number_of_individuals <= max_pupulation

    selected: List = select_best_individuals(population, number_of_individuals)

    for individual in population:

        if(len(selected) >= max_pupulation):
            break

        if random.random() < probability:
            selected.append(individual)

    return selected


def select_best_individuals(population: List, number_of_individuals: int) -> List:

    population.sort()

    return [population.pop(0) for _ in range(number_of_individuals)]