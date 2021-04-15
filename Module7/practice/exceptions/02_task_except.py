# Даны номер месяца и номер года. Найдите сколько дней в этом месяце.
# При вводе неверного номера месяца или некорректного значения программа должна сообщить об ошибке
# и попросить ввести корректные данные. Также необходимо учесть високосный или не високосный год.
# Алгоритм проверки на високосный год оформите в виде отдельной функции.
#
# Входная строка содержит два целых числа – номер месяца (возможно, неправильный) и номер года.
import sys

def days_in_year(year):
    if year % 100 == 0:
        is_leap = year // 100 % 4 == 0
    else:
        is_leap = year % 4 == 0
    return 366 if is_leap else 365

while True:
    try:
        year = int( input("year: ") )
        break
    except (ValueError, TypeError):
        print('Неверное значение')
    except (Exception, EOFError) as e:
        print(e)
        sys.exit()

while True:
    try:
        month = int( input("m: ") )
        if 1 <= month <= 12:
            break
        else:
            raise ValueError
    except (ValueError, TypeError):
        print('Неверное значение')
    except (Exception, EOFError) as e:
        print(e)
        sys.exit()

days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
if month == 2 and days_in_year(year) == 366:
    print(29, "days")
else:
    print(days[month-1], "days")
