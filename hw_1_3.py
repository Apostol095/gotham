"""Запросить у пользователя целое число.
Вывести на экран число в представлении целого числа, вещественного числа, логического значения, строки.
Запросить у пользователя ещё одно целое число.
Выполнить операции + и * над всеми вариантами представления первого числа и второго числа, если они допустимы.
Результаты операций вывести на экран, сопровождая вразумительным текстом о то какая операция над какими типами
операндов была выполнена."""

first_number = int(input('Введите первое целое число: '))
print ('Целое = ' , int (first_number))
print ('Вещественное =' , float (first_number))
print ('Логическое = ' , bool (first_number))
print ('Строка =' , str (first_number))
second_number = int (input('Введите второе целое число: '))
print('Целое + Целое = ', int (first_number) + int (second_number))
print('Целое * Целое = ', int (first_number) * int (second_number))
print('Целое + Вещественное = ', int (first_number) + float (second_number))
print('Целое * Вещественное = ', int (first_number) * float (second_number))
print('Строка + Строка = ' , str(first_number) + str(second_number)) #конкатенация
print('Логическое + Логическое = ' , bool(first_number) + bool (second_number))