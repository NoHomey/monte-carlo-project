import random
from typing import List

from generator import Generator
from genetic_operations import GeneticOperations
from individual import Individual


def main_algorithm(min_population: int, max_population: int, num_iterations: int, limit: float,
                   genetic_operations: GeneticOperations, mutation_probability: float, selection_probability: float):

    assert min_population <= max_population
    assert limit > 0

    Generator.set_limits(-limit, limit)

    start_tolerance = 0.3 * limit

    decreasing_step_tolerance = start_tolerance / num_iterations

    current_tolerance = start_tolerance

    population: List = generate_population(genetic_operations, min_population)

    for iteration in range(num_iterations):
        mutate_population(genetic_operations, population, mutation_probability, current_tolerance)
        next_generation = generate_population(genetic_operations, min_population)
        population.extend(next_generation)
        population = select_individuals(population, min_population, max_population, selection_probability)
        current_tolerance -= decreasing_step_tolerance

    return population

def generate_population(genetic_operations: GeneticOperations, size: int) -> List:

    population: List = [genetic_operations.generate() for _ in range(size)]

    return population


def mutate_population(genetic_operations: GeneticOperations, population: List, probability: float, tolerance: float) -> List:
    
    count = len(population)

    values_count = genetic_operations.generators_len

    for i in range(count):
        if random.random() < probability:
            mutation_probability = random.random()
            step = 1 / values_count
            current = step
            for j in range(values_count):
                if mutation_probability < current:
                    mutant = mutate_individual(genetic_operations, population[i], j, tolerance)
                    population.append(mutant)
                    break
                current += step
    
    return population

def mutate_individual(genetic_operations: GeneticOperations, individual: Individual, value_index: int, tolerance: float) -> Individual:
    assert tolerance > 0

    values = individual.values
    while True:
        change_in_value = random.uniform(-tolerance, tolerance)
        new_value = individual.values[value_index] + change_in_value
        if genetic_operations.is_in_range(new_value, value_index):
            if random.random() < 0.7:
                return genetic_operations.change(values, value_index, new_value)
            else:
                return genetic_operations.mutate(values, value_index)

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