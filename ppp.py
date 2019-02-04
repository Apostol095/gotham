from datetime import datetime
from dateutil import relativedelta
my_date = datetime(2019, 1, 31)
# ask user name
person_name = input('name:')
person_lastname = input('lastname:')
print ("Hello {0} {1}" . format(person_lastname, person_name))
#person birthday
person_birthday = input ('Please enter your day of birthday:')
person_birthmonth = input ('Please enter your month of birthday:')
person_birthyear = input ('Please enter your year of birthday:')
person_birthday = int(person_birthday)
person_birthmonth = int(person_birthmonth)
person_birthyear = int (person_birthyear)
def calculate_age(born):
    today = date.today()
    return today.year - person_birthyear - ((today.month, today.day) < (person_birthmonth, person_birthday))

age = calculate_age(my_date)

print(age)