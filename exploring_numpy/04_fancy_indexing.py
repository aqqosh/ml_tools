import numpy as np

rand = np.random.RandomState(42)
x = rand.randint(100, size=10)

a = [x[3], x[7], x[2]]

ind = [3, 7, 2]
b = x[ind]

a == b

X = np.arange(12).reshape(3, 4)
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])

X[row, col]
X[row[:, np.newaxis], col]

row[:, np.newaxis] * col

