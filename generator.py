from random import uniform, vonmisesvariate
from sys import float_info
import math

class Generator:
    def __init__(self, left, right = float_info.max):
        self.left = left
        self.right = right

    def generate(self):
        return uniform(self.left, self.right)

positive = Generator(float_info.epsilon, float_info.max)

unboud = Generator(float_info.min, float_info.max)

absolute = Generator(0, float_info.max)

radian = Generator(0, 2 * math.pi)

inverse_trigonometric = Generator(-1, 1)

arccosh = Generator(1, float_info.max)

def intersect(genA, genB):
    return Generator(max(genA.left, genB.left), min(genA.right, genB.right))
