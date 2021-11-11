import numpy as np

##############################
#        CONCATENATE
##############################

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])

np.concatenate([x, y])

z = np.array([99, 99, 99])
print(np.concatenate([x, y, z]))

#N dimentions
grid = np.array([[1, 2, 3], 
                [4, 5, 6]])

np.concatenate([grid, grid])
np.concatenate([grid, grid], axis=1)

x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7], [6, 5, 4]])
np.vstack([x, grid])

y = np.array([[99], [99]])
np.hstack([grid, y])

#np.dstack по третьей оси

a = np.arange(12)**2
i = np.array([1, 1, 3, 8, 5])
a[i]

j = np.array([[3, 4], [9, 7]])
a[j]

palette = np.array([[0, 0, 0],
                    [255, 0, 0], 
                    [0, 255, 0],
                    [0, 0, 255],
                    [255, 255, 255]])

image = np.array([[0, 1, 2, 0],
                    [0, 3, 4, 0]])

palette[image]