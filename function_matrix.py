import math

from generator import unboud, absolute, intersect
from relation_symbol import RelationSymbol
from matrix_entry import MatrixEntry
from function import positive_id

def obtain_generators(matrix):
    cols = len(matrix)
    rows = len(matrix[0])
    generators = []
    for j in range(rows):
        generator = unboud
        for i in range(cols):
            generator = intersect(generator, matrix[i][j].function.generator)
        generators.append(generator)
    return generators

def normalize(matrix, rel_symbols, values):
    cols = len(matrix)
    rows = len(matrix[0])
    for i in range(cols):
        rel_symbol = rel_symbols[i]
        if rel_symbol != RelationSymbol.Equal:
            coefient = 1 if rel_symbol == RelationSymbol.LessThanOrEqual else -1
            for k in range(cols):
                matrix[k].append(MatrixEntry(coefient if i == k else 0, positive_id))

def evaluate(matrix, generators):
    while True:
        try:
            cols = len(matrix)
            rows = len(matrix[0])
            values = []
            for i in range(rows):
                values.append(generators[i].generate())
            result = []
            for i in range(cols):
                row_sum = 0
                for j in range(rows):
                    value = matrix[i][j].function.function(values[j])
                    coeficient = matrix[i][j].coeficient
                    row_sum += coeficient * value
                result.append(row_sum)
            return result
        except:
            # overflow error, ignore and try again
            pass

def __dustance_func_helper__(a, b, p):
    sum = 0.0
    for i in range(len(a)):
        # | a - b | ^ p
        sum += math.abs(a[i] - b[i]) ** p

    return sum ** (1.0 / p)
    
def distance(p):
    return lambda a, b: __dustance_func_helper__(a, b, p)
