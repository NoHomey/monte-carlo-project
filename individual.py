class Individual:
    def __init__(self, values, score):
        self.values = values
        self.score = score

def create_individual(values, result, distance_function, target):
    score = distance_function(result, target)
    return Individual(values, score)

def individual_creator(distance_function):
    return lambda values, result, target: create_individual(values, result, distance_function, target)