import numpy as np
import matplotlib.pyplot as plt

# Функция, которую мы хотим построить
def func(x):
    return x**2 + 2*x - 3

# Создаем массив точек
data = np.random.randint(0, 10, size=(100, 4))  # Гистограмма распределения значений от 0 до 10

# Строим гистограмму
plt.hist(data, bins=50, density=True)
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Распредель')