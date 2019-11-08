a = 3.0
r = 4.0
x = [a, 1.0]

def power_outer(r = 1.0):
    def power_inner(x = [1.0, 1.0]):
        return [x[0]**r, r*x[0]**(r-1.0)*x[1]]
    return power_inner

myfunction = power_outer(4.0)
print myfunction(x)
