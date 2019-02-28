"""Пользователь вводит порядковый номер Числа Фибоначчи - n
Программа вычисляет этот элемент ряда Фибоначчи и выводит его на экран (с вразумительным сообщением)."""


def main ():
    n = input("порядковый номер элемента ряда Фибоначчи: ")
    n = int(n)
    res = get_fibonachi(n)
    print('Элемент {} ряда Чисел Фибоначчи = {}' .format(n , res))
def get_fibonachi(n):
   if n == 1:
      return 1
   elif n == 0:
      return 0
   else:
      return get_fibonachi(n-1) + get_fibonachi(n-2)
main()
