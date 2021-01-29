# Даны номер месяца и номер года. Найдите сколько дней в этом месяце.
# При вводе неверного номера месяца или некорректного значения программа должна сообщить об ошибке
# и попросить ввести корректные данные. Также необходимо учесть високосный или не високосный год.
# Алгоритм проверки на високосный год оформите в виде отдельной функции.
#
# Входная строка содержит два целых числа – номер месяца (возможно, неправильный) и номер года.
while True:
    try:
        month = int(input("month: "))
        if not 1 <= month <= 12:
            raise ValueError
        year = int(input("year: "))
    except ValueError:
        print("incorrect data, please try again")
    else:
        break

# if (year%4 == 0 and year%100 != 0) or (year%100 == 0 and year%400 == 0):
#     print('високосный')

thirty_one = (1, 3, 5, 7, 8, 10, 12)
thirty = (4, 6, 9, 11)
for el in thirty_one:
    if month == el:
        print("31")
for el in thirty:
    if month == el:
        print("30", el)
if month == 2 and (year%4 == 0 and year%100 != 0) or (year%100 == 0 and year%400 == 0):
    print("29")
elif month == 2:
    print("28")
