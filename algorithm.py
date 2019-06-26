import heapq
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


def select_best_individuals(population: List, number_of_individuals: int) -> List:

    population.sort()

    return [population.pop(0) in range(number_of_individuals)]