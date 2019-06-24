from generator import unboud, intersect

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

def evaluate(matrix, generators):
    cols = len(matrix)
    rows = len(matrix[0])
    values = []
    for i in range(rows):
        values.append(generators[i].generate())
    result = []
    for i in range(cols):
        row = []
        for j in range(rows):
            row.append(matrix[i][j].function.function(values[j]))
        result.append(row)
    return result
