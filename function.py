import generator
import math

class Function:
    def __init__(self, generator, function):
        self.generator = generator
        self.function  = function

class Power(Function):
    def __init__(self, r):
        super().__init__(generator.positive, lambda x : math.pow(x, r))

class Exponential(Function):
    def __init__(self, a):
        super().__init__(generator.unboud, lambda x: math.pow(a, x))

sqrt    = Function(generator.absolute, lambda x: math.sqrt(x))

ln      = Function(generator.positive, lambda x: math.log(x))

log2    = Function(generator.positive, lambda x: math.log2(x))

log10   = Function(generator.positive, lambda x: math.log10(x))

exp     = Function(generator.unboud, lambda x: math.exp(x))

sin     = Function(generator.radian, lambda x: math.sin(x))

cos     = Function(generator.radian, lambda x: math.cos(x))

tan     = Function(generator.radian, lambda x: math.tan(x))

arcsin  = Function(generator.inverse_trigonometric, lambda x: math.asin(x))

arccos  = Function(generator.inverse_trigonometric, lambda x: math.acos(x))

arctan  = Function(generator.unboud, lambda x: math.atan(x))

sinh    = Function(generator.unboud, lambda x: math.sinh(x))

cosh    = Function(generator.unboud, lambda x: math.cosh(x))

tanh    = Function(generator.unboud, lambda x: math.tanh(x))

arcsinh = Function(generator.unboud, lambda x: math.asinh(x))

arccosh = Function(generator.arccosh, lambda x: math.acosh(x))

arctanh = Function(generator.inverse_trigonometric, lambda x: math.atanh(x))
