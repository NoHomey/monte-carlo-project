def __generate_values__(generators):
    count = len(generators)
    values = []
    for i in range(count):
        value = generators[i].generate()
        values.append(value)
    return values

def generate(evaluate, generators, creator, target):
    return __create_individual__(evaluate, __generate_values__, generators, creator, target)

def __mutate_values__(values, index, generators):
    new_values = values.copy()
    new_values[index] = generators[index].generate()
    return new_values

def mutate(evaluate, generators, values, index, creator, target):
    values_creator = lambda generators: __mutate_values__(values, index, generators)
    return __create_individual__(evaluate, values_creator, generators, creator, target)

def __create_individual__(evaluate, values_creator, generators, individual_creator, target):
    while True:
        try:
            values = values_creator(generators)
            result = evaluate(values)
            return individual_creator(values, result, target)
        except:
            pass
        #except Exception as inst:
        #    print(type(inst))    # the exception instance
        #    print(inst.args)     # arguments stored in .args
        #    print(inst)
        #    raise inst