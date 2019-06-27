import function
import function_matrix
from matrix_entry import MatrixEntry
from relation_symbol import RelationSymbol
from genetic_operations import GeneticOperations
from distance import distance
from individual import individual_creator
from algorithm import main_algorithm, generate_population

matrix = [
    [MatrixEntry(2, function.sin), MatrixEntry(3, function.Power(3))],
    [MatrixEntry(-1, function.log2), MatrixEntry(100, function.arcsin)]
]

rel_symbols = [RelationSymbol.GreaterThanOrEqual, RelationSymbol.LessThanOrEqual]

target = [2, 3]

function_matrix.normalize(matrix, rel_symbols, target)

generators = function_matrix.obtain_generators(matrix)

creator = individual_creator(distance(2))

evaluate = function_matrix.evaluate(matrix)

genetic_operations = GeneticOperations(evaluate, generators, creator, target)

min_population = 20

max_population = 200

num_iterations = 5000

mutation_probability = 0.3

selection_probability = 0.4

limit = 100

population = generate_population(genetic_operations, min_population)

for i in range(10):
    population = main_algorithm(population, min_population, max_population, num_iterations, limit, genetic_operations, mutation_probability, selection_probability)
    limit *= 10

print(population[0])

print(population[0].values)