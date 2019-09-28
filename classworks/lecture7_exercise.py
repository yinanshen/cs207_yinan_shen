import numpy as np
class Circle:
    '''A class for circles
      Constructor is initialized with two tuples, one for the center of the circle
      and the other for a point on the circle.

      Methods include radius, area, and circum.  None of these methods accept any arguments.

      The user is not required to pre-compute the radius of the circle.  Exception testing is
      done in area and circum to check for a circle radius.  If it doesn't exist, a radius is
      computed.
    '''

    def __init__(self, center, point):
        self.xc = center[0]
        self.yc = center[1]
        self.x = point[0]
        self.y = point[1]

    def radius(self):
        x = self.x - self.xc
        y = self.y - self.yc
        self.R = np.sqrt(x * x + y * y)

    def area(self):
        try:
            self.A = np.pi * self.R* self.R
        except AttributeError:
            x = self.x - self.xc
            y = self.y - self.yc
            r = np.sqrt(x * x + y * y)
            self.R = r
            self.A = np.pi * r * r
        return self.A

    def circum(self):
        try:
            self.C =  2.0 * np.pi * self.R
        except AttributeError:
            x = self.x - self.xc
            y = self.y - self.yc
            r = np.sqrt(x * x + y * y)
            self.R = r
            self.C = 2.0 * np.pi * r

        return self.C

class Rcircle(Circle):
    def __init__(self, radius):
        self.r = radius
        self.R = radius

    def radius(self):
        self.R = self.r
        return self.R
    def __eq__(self, theother):
        return self.R == theother.R

a = Rcircle(radius = 1)
print(a.radius(),' is the radius of a circle')
print(a.circum(),' is the circum of a circle')
print(a.area(),' is the area of a circle')
b = Rcircle(radius = 2)
c = Rcircle(radius = 2)
print('That the circle with radius 1 is equal to the circle with radius 2 is', a == b)
