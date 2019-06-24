import generator
import math

class Function:
    def __init__(self, generator, function, description = ""):
        self.generator   = generator
        self.function    = function
        self.description = description

    def __str__(self):
        return self.description

    def __repr__(self):
        return self.__str__()

class Power(Function):
    def __init__(self, r):
        super().__init__(generator.positive, lambda x : math.pow(x, r))
        self.r = r

    def __str__(self):
        return "x^" + str(self.r)

class Exponential(Function):
    def __init__(self, a):
        super().__init__(generator.unboud, lambda x: math.pow(a, x))
        self.a = a

    def __str__(self):
        return str(self.a) + "^x"

sqrt    = Function(generator.absolute, lambda x: math.sqrt(x), "√(x)")

ln      = Function(generator.positive, lambda x: math.log(x), "ln(x)")

log2    = Function(generator.positive, lambda x: math.log2(x), "log2(x)")

log10   = Function(generator.positive, lambda x: math.log10(x), "log10(x)")

exp     = Function(generator.unboud, lambda x: math.exp(x), "e^x")

sin     = Function(generator.radian, lambda x: math.sin(x), "sin(x)")

cos     = Function(generator.radian, lambda x: math.cos(x), "cos(x)")

tan     = Function(generator.radian, lambda x: math.tan(x), "tan(x)")

arcsin  = Function(generator.inverse_trigonometric, lambda x: math.asin(x), "arcsin(x)")

arccos  = Function(generator.inverse_trigonometric, lambda x: math.acos(x), "arccos(x)")

arctan  = Function(generator.unboud, lambda x: math.atan(x), "arctan(x)")

sinh    = Function(generator.unboud, lambda x: math.sinh(x), "sinh(x)")

cosh    = Function(generator.unboud, lambda x: math.cosh(x), "cosh(x)")

tanh    = Function(generator.unboud, lambda x: math.tanh(x), "tanh(x)")

arcsinh = Function(generator.unboud, lambda x: math.asinh(x), "arcsinh(x)")

arccosh = Function(generator.arccosh, lambda x: math.acosh(x), "arccosh(x)")

arctanh = Function(generator.inverse_trigonometric, lambda x: math.atanh(x), "arctanh(x)")

positive_id = Function(generator.absolute, lambda x: x, "x")