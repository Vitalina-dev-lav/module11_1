

import numpy as np

a = np.array([1, 2, 3])
a_multiplication = a * 2  # Умножение массива на число
print(f'a = {a}')
print(f'a_multiplication={a_multiplication}')
print(a.size)  # выводим кол-во элементов массива a

# Создаем массивы из целых случайных чисел
b = np.random.randint(5, size=4)
c = np.random.randint(1, 10, size=(2, 5))

print(f'b = {b}')
print(f'c = {c}')

#  Перемножаем матрицы

d = np.arange(1, 10).reshape(3, 3)
print(f'd = {d}')
x = np.dot(a, d)  # Умножаем вектор на матрицу
y = np.dot(d, a)  # Умножаем матрицу на вектор

print(f'x = {x}')

print(f'y = {y}')
