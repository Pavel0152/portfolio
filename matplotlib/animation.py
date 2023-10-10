import numpy as np
from matplotlib import pyplot as plt

# Задаем координаты и скорость объекта
x = np.linspace(0, 100, 1000)  # задаем начальные координаты и скорость
vx = 0.1 * x  # задаем вектор скорости
vy = 0.3 * x  # задаем вектор скорости

# Создаем объект и рисуем его на графике
fig, ax = plt.subplots()
ax.plot(x, vx, 'r-', label='Координаты объекта')
ax.plot(x, vy, 'b--', label='Скорость объекта')
ax.set_xlim([0, 100])
ax.set_ylim([0, 100])
ax.legend()

# Добавляем анимацию перемещения объекта
plt.show()