import function
import function_matrix
from matrix_entry import MatrixEntry
from relation_symbol import RelationSymbol
from genetic_operations import GeneticOperations
from distance import distance
from individual import individual_creator
from generator import Generator
from algorithm import generate_population, mutate_population

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

Generator.set_limits(-100, 100)

population = generate_population(genetic_operations, 5)

print(population)

mutate_population(genetic_operations, population, 0.3)

print(population)