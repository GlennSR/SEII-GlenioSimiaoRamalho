import numpy as np
import matplotlib.pyplot as plt

# CREATING ARRAYS
a1 = np.array([3, 5, 7, 3])
a2 = np.zeros(10)
a3 = np.ones(10)
a4 = np.random.random(10)
a5 = np.random.randn(10)
a6 = np.linspace(0, 10, 100)
a7 = np.arange(0, 10, 0.2)

# ARRAY OPERATIONS
a1 * 2
1 / a1
a1 > 4
print(2 * a1 > 10)
print(1 / a1 + a1 + 2)

x = np.linspace(0, 1, 1000)
print(x**2)
y = x**2
plt.plot(x, y)
plt.hist(a4)
plt.show()


def f(x):
    return x**2 * np.sin(x) / np.exp(-x)


y = f(x)
plt.plot(x, y)
plt.show()
