from random import uniform, vonmisesvariate
import math

__epsilon__ = 0.0000000001

class Generator:
    max_value = 10000000000000
    min_value = -max_value

    @staticmethod
    def set_limits(min_value, max_value):
        Generator.min_value = min_value
        Generator.max_value = max_value

    def __init__(self, left, right = "max"):
        self.left = left
        self.right = right

    def generate(self):
        left = Generator.min_value if self.left == "min" else self.left
        right = Generator.max_value if self.right == "max" else self.right
        return uniform(left, right)

positive = Generator(__epsilon__, "max")

unboud = Generator("min", "max")

absolute = Generator(0, "max")

radian = Generator(0, 2 * math.pi)

inverse_trigonometric = Generator(-1, 1)

arccosh = Generator(1, "max")

def intersect(genA, genB):
    return Generator(__max__(genA.left, genB.left), __min__(genA.right, genB.right))

def __extreme__(tmp, func, a, b):
    if a == tmp:
        return b
    else:
        if b == tmp:
            return a
        else:
            return func(a, b)

def __max__(a, b):
    return __extreme__("min", max, a, b)

def __min__(a, b):
    return __extreme__("max", min, a, b)