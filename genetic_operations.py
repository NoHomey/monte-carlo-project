from function_matrix import evaluate

def __generate_values__(count, generators):
    count = len(generators)
    values = []
    for i in range(count):
        values.append(generators[i].generate())
    return values

def generate(matrix, generators, creator, target):
    return __create_individual__(matrix, __generate_values__, generators, creator, target)

def __mutate_values__(values, index, generators):
    new_values = values.copy()
    new_values[index] = generators[index].generate()

def mutate(matrix, generators, values, index, creator, target):
    values_creator = lambda generators: __mutate_values__(values, index, generators)
    return __create_individual__(matrix, values_creator, generators, creator, target)

def __create_individual__(matrix, values_creator, generators, individual_creator, target):
    while True:
        try:
            values = values_creator(generators)
            result = evaluate(matrix, values)
            return individual_creator(values, result, target)
        except:
            # overflow error, ignore and try again
            pass