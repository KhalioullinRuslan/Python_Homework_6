# Задача HARD SORT необязательная. 
# Задайте двумерный массив из целых чисел. 
# Количество строк и столбцов задается с клавиатуры. 
# Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10

from random import randint
arraySize = [int(v) for v in input('Размер двумерного массива через пробел: ').split()]
print(arraySize)
arrayRaw = []
for i in range(arraySize[0]):
    arrayRaw.append([randint(1, 20) for _ in range(arraySize[1])])
print(arrayRaw)