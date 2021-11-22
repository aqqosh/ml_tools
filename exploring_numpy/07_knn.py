import numpy as np
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

rand = np.random.RandomState(42)
X = rand.rand(10,2)

plt.scatter(X[:, 0], X[:, 1], s = 100)
plt.show()

differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]
sq_differences = differences ** 2
dist_sq = sq_differences.sum(-1)

dist_sq.diagonal()

nearest = np.argsort(dist_sq, axis=1)

K = 2
nearest_partirion = np.argpartition(dist_sq, K+1, axis=1)
