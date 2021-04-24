# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

month = int(input("Please input a month: "))

if 1<=month<=2 or month==12:
    print ("WINTER")
elif 3<=month<=5:
    print ("SPRING")
elif 6<=month<=8:
    print ("SUMMER")
elif 9<=month<=11:
    print ("AUTUMN")
