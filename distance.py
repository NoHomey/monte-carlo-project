import math

def __dustance_func_helper__(a, b, p):
    sum = 0.0
    for i in range(len(a)):
        # | a - b | ^ p
        d = abs(a[i] - b[i])
        sum += d ** p

    return sum ** (1.0 / p)
    
def distance(p):
    return lambda a, b: __dustance_func_helper__(a, b, p)