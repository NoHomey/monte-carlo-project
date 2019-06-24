class MatrixEntry:
    def __init__(self, coeficient, function):
        self.coeficient = coeficient
        self.function   = function

    def __str__(self):
        return str(self.coeficient) + self.function.__str__()

    def __repr__(self):
        return self.__str__()
