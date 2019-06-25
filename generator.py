from random import uniform, vonmisesvariate
import math

__epsilon__ = 0.0000000001

__max__ = 10000000000

__min__ = -__max__

class Generator:
    def __init__(self, left, right = __max__):
        self.left = left
        self.right = right

    def generate(self):
        return uniform(self.left, self.right)

positive = Generator(__epsilon__, __max__)

unboud = Generator(__min__, __max__)

absolute = Generator(0, __max__)

radian = Generator(0, 2 * math.pi)

inverse_trigonometric = Generator(-1, 1)

arccosh = Generator(1, __max__)

def intersect(genA, genB):
    return Generator(max(genA.left, genB.left), min(genA.right, genB.right))
