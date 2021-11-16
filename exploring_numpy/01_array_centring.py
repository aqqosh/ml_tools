import numpy as np

X = np.random.random((10, 3))

X_mean = X.mean(0)
X_centred = X- X_mean
X_centred.mean(0)
