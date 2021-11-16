import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))

# Число элементов массива < 6
np.count_nonzero(x < 6)
np.sum(x < 6)

# Число значений < 6 в каждой строке
np.sum(x < 6, axis=1)

# Проверка всех значений массива
np.any(x > 8)
np.all(x < 10)

# И для каждой строки тоже
np.any(x > 0, axis=1)

# Немного более реальные данные

rainfall = pd.read_csv("ml_tools/exploring_numpy/data/seattle2014.csv")["precipitation"].values
inches = rainfall / 254
inches.shape

plt.hist(inches, 40)
plt.show()

