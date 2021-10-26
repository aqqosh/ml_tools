import numpy as np

##############################
#         FROM LISTS
##############################

# array from list
test_list = [0, 1, 2, 3, 4]
test_arr = np.array(test_list)

# fixed data type in the list
mixed_list = [0, 1.2, 12, 0.13]
test_arr = np.array(mixed_list)

# dtype
int_list = [0, 1, 2, 3, 4]
test_arr = np.array(int_list, dtype=np.float32)

# n-dimetions
n_arr = np.array([range(i, i+3) for i in [2, 4, 6]])

##############################
#        FROM SCRATCH
##############################

np.zeros(10, dtype = int)
np.ones((3, 5), dtype = float)
np.full((3, 5), 3.14)

np.arange(0, 20, 2)
np.linspace(0, 1, 5)
np.random.random((3, 3))

np.random.normal(0, 1, (3, 3)) # 0 - median, 1 - std
np.eye(3)

##############################
#     ARRAY'S ATTRIBUTES
##############################

# начальное значение для воспроизводимости
np.random.seed(0)

x1 = np.random.randint(10, size=6) # n=1
x2 = np.random.randint(10, size=(4, 5)) # n=2
x3 = np.random.randint(10, size=(3, 4, 5)) # n=3

# main attributes
for example in [x1, x2, x3]:
    meaning_str = "dim = {}, shape = {}, size = {}, dtype = {}".format(
        example.ndim, example.shape, example.size, example.dtype)
    print(meaning_str)

# more attributes
for example in [x1, x2, x3]:
    meaning_str = "itemsize = {}, nbytes = {}".format(
        example.itemsize, example.nbytes)
    print(meaning_str)







