def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b

def div(a,b):
    return a/b

calc_dict = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}


def main():
    check1= True
    while check1 == True:
        try:
            first_number = float(input('Введите первое число: '))
            check1 = False
        except ValueError:
            print('Ошибка.Введите число еще раз: ')
    operation_chek = True
    while operation_chek == True:
        try:
            operation = input('Выберете операцию из доступных: ' + str(list(calc_dict.keys()))).strip()
            if "+" and "-" and '*' and '/' not in operation:
                continue
            operation_chek = False
            break
        except (KeyError, ValueError) :
            print('Сделайте выбор еще раз ')
    check2= True
    while check2 == True:
        try:
            second_number = float(input('Введите второе число: '))
            check2 = False
        except ValueError:
            print('Ошибка.Введите число еще раз: ')
    res = None
    if operation in calc_dict.keys():
        res  = calc_dict[operation](first_number , second_number) # add(first_number , second_number)
    if res is not None:
        print('Результат = ', res)

main()
#check()