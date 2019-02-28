"""Пользователь вводит два числа a и b. Тип чисел может быть как int(), так и float()
Выведите сумму всех натуральных чисел от меньшего до большего (включительно).
Рекомендую строго соблюдать определние "натуральное число"""


def main():
    a = input('Введите число: ')
    b = input('Введите число: ')
    a = int(float(a))
    b = int(float(b))
    summa = sum_natural_numbers(a, b)
    print(summa)


def sum_natural_numbers(a, b):
    s = 0
    if a > b:
        for i in range(abs(b), abs(a + 1)):
            s = s + i
    else:
        for x in range(abs(a), abs(b + 1)):
             s = s + x
    return s
main()
