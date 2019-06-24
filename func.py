import generator
import math

class Func:
    def __init__(self, gen, f):
        self.gen = gen
        self.f = f

class Power(Func):
    def __init__(self, r):
        super().__init__(generator.positive, lambda x : math.pow(x, r))

class Exponential(Func):
    def __init__(self, a):
        super().__init__(generator.unboud, lambda x: math.pow(a, x))

sqrt = Func(generator.absolute, lambda x: math.sqrt(x))

ln = Func(generator.positive, lambda x: math.log(x))

log2 = Func(generator.positive, lambda x: math.log2(x))

log10 = Func(generator.positive, lambda x: math.log10(x))

exp = Func(generator.unboud, lambda x: math.exp(x))

sin = Func(generator.radian, lambda x: math.sin(x))

cos = Func(generator.radian, lambda x: math.cos(x))

tan = Func(generator.radian, lambda x: math.tan(x))

arcsin = Func(generator.inverse_trigonometric, lambda x: math.asin(x))

arccos = Func(generator.inverse_trigonometric, lambda x: math.acos(x))

arctan = Func(generator.unboud, lambda x: math.atan(x))

sinh = Func(generator.unboud, lambda x: math.sinh(x))

cosh = Func(generator.unboud, lambda x: math.cosh(x))

tanh = Func(generator.unboud, lambda x: math.tanh(x))

arcsinh = Func(generator.unboud, lambda x: math.asinh(x))

arccosh = Func(generator.arccosh, lambda x: math.acosh(x))

arctanh = Func(generator.inverse_trigonometric, lambda x: math.atanh(x))
