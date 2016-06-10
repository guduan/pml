from __future__ import division
from numpy.polynomial.polynomial import Polynomial

class Conversion(object):

    def __init__(self):
        self.hw_units = ''
        self.phys_units = ''

    def to_phys(self, hw_value):
        return hw_value

    def to_hw(self, phys_value):
        return phys_value


class PolyConversion(Conversion):

    def __init__(self, coeffs):
        self._poly = Polynomial(coeffs)

    def to_phys(self, hw_value):
        raise Exception('Not invertible')

    def to_hw(self, hw_value):
        return self._poly(hw_value)


class LinearConversion(PolyConversion):

    def __init__(self, x, y):
        super(LinearConversion, self).__init__((x, y))

    def to_phys(self, hw_value):
        x = (hw_value - self._poly.coef[0]) / self._poly.coef[1]
        return x

    def to_hw(self, hw_value):
        return self._poly(hw_value)
