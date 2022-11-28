# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform


n = int(input('Введите размер списка: '))
ass = []
for i in range(n):
    f = uniform(0, 9)
    ass.append(round(f, 2))

min = ass[0]
max = 0
for i in range(len(ass)):
    if max < ass[i]:
        max = ass[i]
    if min > ass[i]:
        min = ass[i]

dif = (max - int(max)) - (min - int(min))

result = round(dif, 2)
print(ass)
print(f'Минимальное значение: {min}')
print(f'Максимальное значение: {max}')
print(f'Разница между значениями: {result}')