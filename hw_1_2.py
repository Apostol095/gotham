"""Запросить у пользователя число1 (число может быть любое).
Запросить у пользователя число2 (число может быть любое).
Вывести результат всех известных Вам допустимых операций над двумя числами."""
first_number= float(input('Введите любое первое число: '))
second_number = float (input('Введите любое второе число: '))
print ( 'Сложение двух чисел :' , first_number + second_number)
print ( 'Вычитание двух чисел: :' , first_number - second_number)
print ( 'Умножение двух чисел :' , first_number * second_number)
print ( 'Деление двух чисел :' , first_number / second_number)
print ( 'Целочисленное деление двух чисел :' , first_number // second_number)
print ( 'Возведение в степень :' , first_number ** second_number)
print ( 'Получение остатка от деления: :' , first_number % second_number)