from random import random
from typing import List

from genetic_operations import GeneticOperations


def main_algorithm(min_population: int, max_population: int, num_iterations: int, start_tolerance: float,
                   genetic_operations: GeneticOperations):

    decreasing_step_tolerance = start_tolerance / num_iterations

    current_tolerance = start_tolerance

    initial_population: List = create_initial_population(genetic_operations, min_population)


def create_initial_population(genetic_operations: GeneticOperations, size: int) -> List:

    population: List = [genetic_operations.generate() for _ in range(size)]

    return population


def select_individuals(population: List, number_of_individuals: int,  max_pupulation: int, probability: float) -> List:

    assert number_of_individuals <= max_pupulation

    selected: List = select_best_individuals(population, number_of_individuals)

    for individual in population:

        if(max_pupulation > len(selected)):
            break

        if random.random() < probability:
            selected.append(individual)
            
    return selected


def select_best_individuals(population: List, number_of_individuals: int) -> List:

    population.sort()

    return [population.pop(0) in range(number_of_individuals)]