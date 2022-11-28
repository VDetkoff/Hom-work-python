# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint

number = int(input('Введите размер списка '))

list = []
sum = 0

for i in range(number):
    list.append(randint(0, 9))
    if i % 2 != 0:
        sum += list[i]

print(list)
print(f'Сумма нечетных чисел равна {sum}')