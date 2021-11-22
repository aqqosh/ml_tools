import numpy as np
from numba import cuda

# data creation
n = 16384 # matrix side size
threads_per_block = 256
blocks = int(n / threads_per_block)

# input matrix
a = np.ones(n*n).reshape(n,n).astype(np.float32)
# here we set an arbitrary row to an arbitrary value
a[3] = 9

# output vector
sums = np.zeros(n).astype(np.float32)

d_a = cuda.to_device(a)
d_sums = cuda.to_device(sums)

# kernel definition
@cuda.jit
def row_sums(a, sums, ds):
    idx = cuda.grid(1)
    sum = 0.0

    for i in range(ds):
        sum += a[i][idx]

    sums[idx] = sum

row_sums[blocks, threads_per_block](d_a, d_sums, n)
cuda.synchronize()

result = d_sums.copy_to_host()
truth = a.sum(axis=1)
np.array_equal(truth, result)