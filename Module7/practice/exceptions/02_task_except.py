# Даны номер месяца и номер года. Найдите сколько дней в этом месяце.
# При вводе неверного номера месяца или некорректного значения программа должна сообщить об ошибке
# и попросить ввести корректные данные. Также необходимо учесть високосный или не високосный год.
# Алгоритм проверки на високосный год оформите в виде отдельной функции.
#
# Входная строка содержит два целых числа – номер месяца (возможно, неправильный) и номер года.

days = [None, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_year(year):
    if year % 4 != 0:
        return True
    else:
        if year % 100 == 0 and year % 400 == 0:
            return False
        return True

while True:
    try:
        in_data = input('Введите данные в формате "m.yyyy":')
        str_data = in_data.split('.')
        print(str_data)
        if len(str_data) != 2 and len(str_data[1]) != 4:
            raise ValueError
        month, year = int(str_data[0]), int(str_data[1])
        
        if get_year(year):
            days[2] = 29
        else:
            days[2] = 28
            
        if  not(0 < month <= 12):
            raise ValueError
    except ValueError:
        print('Некорректные данные! Попробуйте ещё раз..')
    except Exception as err:
        print('Неожиданное исключение:', err)
    else:
        print(days[month])
        break
