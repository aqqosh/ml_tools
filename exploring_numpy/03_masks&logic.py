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


# Немного более реальные данные #

rainfall = pd.read_csv("ml_tools/exploring_numpy/data/seattle2014.csv")["precipitation"].values
inches = rainfall / 254
inches.shape

plt.hist(inches, 40)
plt.show()

np.sum((inches > 0.05) & (inches < 0.1))

print("Number days without of rain: ", np.sum(inches == 0))
print("Number days with rain: ", np.sum(inches != 0))
print("Days with more than 0.5 inches ", np.sum(inches >= 0.5))
print("Rainy days with < 0.1 inches ", np.sum((inches > 0) & (inches < 0.2)))

# Маскирование
x[x < 5]

rainy = (inches > 0)
summer = (np.arange(365) - 172 < 90) & (np.arange(365) - 172 > 0)
np.median(inches[rainy])
np.median(inches[summer])