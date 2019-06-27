class GeneticOperations:
    def __init__(self, evaluate, generators, individual_creator, target):
        self.evaluate = evaluate
        self.generators = generators
        self.generators_len = len(generators)
        self.individual_creator = individual_creator
        self.target = target

    def generate(self):
        return self.__create_individual__(self.__generate_values__)

    def mutate(self, values, index):
        values_creator = lambda : self.__mutate_values__(values, index)
        return self.__create_individual__(values_creator)

    def is_in_range(self, value, index):
        return self.generators[index].is_in_range(value)

    def change(self, values, index, value):
        new_values = values.copy()
        new_values[index] = value
        try:
            result = self.evaluate(new_values)
            return self.individual_creator(new_values, result, self.target)
        except:
            return self.mutate(values, index)

    def __generate_values__(self):
        values = []
        for i in range(self.generators_len):
            value = self.generators[i].generate()
            values.append(value)
        return values

    def __mutate_values__(self, values, index):
        new_values = values.copy()
        new_values[index] = self.generators[index].generate()
        return new_values

    def __create_individual__(self, values_creator):
        while True:
            try:
                values = values_creator()
                result = self.evaluate(values)
                return self.individual_creator(values, result, self.target)
            except:
                pass
            #except Exception as inst:
            #    print(type(inst))    # the exception instance
            #    print(inst.args)     # arguments stored in .args
            #    print(inst)
            #    raise inst