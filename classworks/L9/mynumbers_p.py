import numpy as np

class RealExtensions:   # ()not necessary
    def __init__(self, a, b):
        self.a = a # attributes
        self.b = b

class _Complex(RealExtensions):
    def __init__(self, a, b):
        self.real = a
        self.imag = b

    def _magnitude(self):
        return np.sqrt(np.square(self.real) + np.square(self.imag))

    def _angle(self):
        return np.arctan(self.imag / self.real)

    def polar_form(self):
        return self._magnitude(), self._angle()

class Dual(RealExtensions):
    def __init__(self, a, b):
        self.real = a
        self.dual = b

    def _magnitude(self):
        return self.real

    def _angle(self):
        return self.dual / self.real

    def polar_form(self):
        return self._magnitude(), self._angle()
