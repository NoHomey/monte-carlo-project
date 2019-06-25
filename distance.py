def __dustance_func_helper__(a, b, p):
    sum = 0.0
    for i in range(len(a)):
        # | a - b | ^ p
        sum += math.abs(a[i] - b[i]) ** p

    return sum ** (1.0 / p)
    
def distance(p):
    return lambda a, b: __dustance_func_helper__(a, b, p)