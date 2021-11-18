import numpy as np

x = np.arange(10)
i = np.array([2, 1, 8, 4])

x[i] = 99
print(x)

x[i] -= 10
print(x)

x = np.zeros(10)
x[[0, 0]] = [4, 6]
print(x)

i = [2, 3, 3, 4, 4, 4]
x[i] += 1
x

x = np.zeros(10)
np.add.at(x, i, 1)
print(x)

