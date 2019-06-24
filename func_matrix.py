from generator import unboud, union

def generators(matrix):
    m = len(matrix)
    n = len(matrix[0])
    gens = []
    for j in range(n):
        gen = unboud
        for i in range(m):
            gen = union(gen, matrix[i][j].gen)
        gens.append(gen)
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
            row.append(matrix[i][j].f(vals[j]))
        res.append(row)
    return res
