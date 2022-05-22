# Сформировать список из N членов последовательности.

from random import randint
N = int(input("Введите колличество элементов списка N: " ))
array = []
for i in range(N):
    array.append(randint(-19,35))
for i in array:
    print(i, end=' ')
print()     
