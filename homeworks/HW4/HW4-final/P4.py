class AutoDiffToy:

    def __init__(self, val, der = 1):  #This would be like the first row in the evaluation trace tables that we've been making.
        self.val = val
        self.der = der

    def __add__(self, beta):
        try:
            if type(beta) == int:
                return AutoDiffToy(self.val + beta, self.der)
            if type(beta) == AutoDiffToy:
                return AutoDiffToy(self.val + beta.val, self.der + beta.der)
        except AttributeError:
            print('The input beta is neither a number nor an AutoDiffToy object.')

    def __radd__(self,beta):
        return self.__add__(beta)

    def __mul__(self, alpha):
        try:
            if type(alpha) == int:
                return AutoDiffToy(self.val * alpha, self.der * alpha)
            if type(alpha) == AutoDiffToy:
                return AutoDiffToy(self.val * alpha.val, self.der * alpha.val + self.val * alpha.der)
        except AttributeError:
            print('The input alpha is neither a number nor an AutoDiffToy object.')

    def __rmul__(self, alpha):
        return self.__mul__(alpha)

'''
a = 1
x = AutoDiffToy(a)
alpha = AutoDiffToy(1)
beta = AutoDiffToy(1)

f = alpha * x + beta
print(f.val, f.der)
f = x * alpha + beta
print(f.val, f.der)
f = beta + alpha * x
print(f.val, f.der)
f = beta + x * alpha
print(f.val, f.der)


a = 1
x = AutoDiffToy(a)
alpha = 1
beta = 1

f = alpha * x + beta
print(f.val, f.der)
f = x * alpha + beta
print(f.val, f.der)
f = beta + alpha * x
print(f.val, f.der)
f = beta + x * alpha
print(f.val, f.der)
'''
