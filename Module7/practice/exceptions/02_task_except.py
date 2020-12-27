# Даны номер месяца и номер года. Найдите сколько дней в этом месяце.
# При вводе неверного номера месяца или некорректного значения программа должна сообщить об ошибке
# и попросить ввести корректные данные. Также необходимо учесть високосный или не високосный год.
# Алгоритм проверки на високосный год оформите в виде отдельной функции.
#
# Входная строка содержит два целых числа – номер месяца (возможно, неправильный) и номер года.
def days_in_year(num_year):
    if num_year % 100 != 0 and num_year % 400 and num_year % 4 == 0:
        return "366"
    return "365"

while True:
    try:
        month = int(input('month'))
        year = int(input('year'))
        if month > 12 and month > 0:
            raise ValueError
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            print(31)
        elif month == 4 or month == 6 or month == 9 or month == 1:
            print(30)
        elif month == 2:
             i = days_in_year(year)
             if i == 365:
                print(28)
             else:
                 print (29)
    except ValueError:
        print('Format error')
    break
