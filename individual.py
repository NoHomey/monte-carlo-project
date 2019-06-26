
class Individual:

    def __init__(self, values, score):
        self.values = values
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "Individual(" + str(self.score) + ")"


def create_individual(values, result, distance_function, target):
    score = distance_function(result, target)
    return Individual(values, score)


def individual_creator(distance_function):
    return lambda values, result, target: create_individual(values, result, distance_function, target)