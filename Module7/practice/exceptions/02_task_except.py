# Даны номер месяца и номер года. Найдите сколько дней в этом месяце.
# При вводе неверного номера месяца или некорректного значения программа должна сообщить об ошибке
# и попросить ввести корректные данные. Также необходимо учесть високосный или не високосный год.
# Алгоритм проверки на високосный год оформите в виде отдельной функции.
#
# Входная строка содержит два целых числа – номер месяца (возможно, неправильный) и номер года.
def days_in_year(num_year):
    if num_year % 4 == 0 and num_year % 100 != 0 or num_year % 400 == 0:
        return True
    return False

days_in_month = (31, 28, 3, 30, 31, 30, 31, 31, 30, 31, 30, 31)
while True:
    try:
        month = float(input('введите месяц'))
        if float(month) % 1 != 0:
            raise ValueError
        month = int(month)
        if month < 1 or month > 12 or :
            raise ValueError
        break
    except ValueError:
        print('некорректные данные')
        
while True:
    try:
        year = float(input('введите год'))
        if float(year) % 1 != 0:
            raise ValueError
        year = int(year)
        break
    except ValueError:
        print('некорректные данные')


days = days_in_month[month - 1]
if month == 2:
    if days_in_year(year):
        days +=1
        
print(days)
