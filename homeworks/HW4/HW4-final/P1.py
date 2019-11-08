import numpy as np
import matplotlib.pyplot as plt

def numerical_diff(f, h):
    def compute_derivative(x):
        return (f(x + h) - f(x))/h
    return compute_derivative

x = np.linspace(0.2, 0.4, 30)

calculate_h1_derivative = numerical_diff(np.log, h = 1e-1)
h1_result = calculate_h1_derivative(x)
plt.plot(x, h1_result, 'b', label = 'h = 1e-1')

calculate_h2_derivative = numerical_diff(np.log, h = 1e-7)
h2_result = calculate_h2_derivative(x)
plt.plot(x, h2_result, 'r', label = 'h = 1e-7')

calculate_h3_derivative = numerical_diff(np.log, h = 1e-15)
h3_result = calculate_h3_derivative(x)
plt.plot(x, h3_result, 'g', label = 'h = 1e-15')

true_derivative = 1/x
plt.plot(x, true_derivative, 'k.', label = 'true derivative')

plt.title('Compare the Closure to the True Derivative')
plt.xlabel('x')
plt.ylabel('Derivative')
plt.legend(loc = 'best')
print("Answer to Q-a: h = 1e-7 most closely approximates the true derivative. ",
      "If h is too small, then the accuracy gets killed by floating point roundoff.",
      "If h is too large, the result will not be correctly represent the true derivative ",
      "and approximation error will be big, because x + h is too far away from x.")
print("Answer to Q-b: Becuase automatic differentiation calculates exact derivatives, "
      "so the accuracy is only limited by floating point error.")
print("For Part 3, the reference is http://www.columbia.edu/~ahd2125/post/2015/12/5/")
plt.show()
