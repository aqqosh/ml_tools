import numpy as np

from numpy import testing
from numba import cuda

@cuda.jit()
def square_device(a, out):
    idx = cuda.grid(1)
    out[idx] = a[idx] * a[idx]

n = 4096
a = np.arange(n)
out = a**2

d_a = cuda.to_device(a) 
d_out = cuda.device_array_like(d_a) 

blocks = 128
threads = 32

square_device[blocks, threads](d_a, d_out)
testing.assert_almost_equal(d_out, out)