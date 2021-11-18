import numpy as np
from numpy import testing

from numba import cuda
from math import hypot

@cuda.jit()
def hypot_stride(a, b, c):
    start = cuda.grid(1)
    stride = cuda.gridsize(1)
    
    for i in range(start, a.shape[0], stride):
        c[i] = hypot(a[i], b[i])

n = 1000000
a = np.random.uniform(-12, 12, n).astype(np.float32)
b = np.random.uniform(-12, 12, n).astype(np.float32)
d_a = cuda.to_device(a)
d_b = cuda.to_device(b)
d_c = cuda.device_array_like(d_b)

blocks = 128
threads_per_block = 64

hypot_stride[blocks, threads_per_block](d_a, d_b, d_c)
testing.assert_almost_equal(np.hypot(a,b), d_c.copy_to_host(), decimal=5)