"""Пользователь вводит два числа a и b. Тип чисел может быть как int(), так и float()
Выведите сумму всех натуральных чисел от меньшего до большего (включительно).
Рекомендую строго соблюдать определние "натуральное число"""
a = int(input('Введите целое первое число: '))
b = int(input('Введите целое второе число: '))
s = 0
for i in range (a, b+1):
    s = s+i
print (s)
