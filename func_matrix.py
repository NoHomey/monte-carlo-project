from generator import unboud, intersect

def generators(matrix):
    m = len(matrix)
    n = len(matrix[0])
    gens = []
    for j in range(n):
        generator = unboud
        for i in range(m):
            generator = intersect(generator, matrix[i][j].generator)
        gens.append(generator)
    return gens

def calc(matrix, gens):
    m = len(matrix)
    n = len(matrix[0])
    vals = []
    for i in range(n):
        vals.append(gens[i].generate())
    res = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(matrix[i][j].function(vals[j]))
        res.append(row)
    return res
