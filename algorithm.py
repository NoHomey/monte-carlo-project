from genetic_operations import GeneticOperations


def main_algorithm(min_population : int, max_population: int, num_iterations : int, start_tolerance : float,
                   genetic_operations : GeneticOperations):

    decreasing_step_tolerance = start_tolerance / num_iterations

    current_tolerance = start_tolerance

    initial_population = create_initial_population(genetic_operations, min_population)

    


def create_initial_population(genetic_operations : GeneticOperations, size : int):

    return [genetic_operations.generate() for x in range(size)]
