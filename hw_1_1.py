"""Запросить у пользователя имя и фамилию.
Поприветсвовать пользователя с использованием его имени и фамилии.
Запросить День даты рождения (цело число).
Запросить Месяц даты рождения (цело число).
Запросить Год даты рождения (цело число).
Вывести количество прожитых лет (цело число).
Вывести количество прожитых месяцев (цело число).
Вывести количество прожитых дней, месяцев, лет до даты начала курса 31.01.2019
 - без учёта високосных лет и считая, что среднее количество дней в месяце = 30."""
my_day = 31
my_month = 1
my_year = 2019
person_name = input('Имя:')
person_lastname = input('Фамилия:')
print ("Привет {0} {1}" . format(person_lastname, person_name))
# person birthday год равно = 12 месяцев умножено на 30 дней итого 360 дней в году
person_birthday = int (input ('Введите день даты рождения: '))
person_birthmonth = int (input ('Введите месяц даты рождения: '))
person_birthyear = int(input ('Ввведите год даты рождения: '))
print('Количество прожитых лет: ' , int(my_year) - int(person_birthyear))
print('Количество прожитых месяцев: ' ,(int((my_year) - int(person_birthyear)) * 12 ) - int(person_birthmonth))
print('Количество прожитых дней: ' , int(((my_year) - int(person_birthyear) ) * 360) - int(person_birthday))
