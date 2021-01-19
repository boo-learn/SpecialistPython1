# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

number = int(input())

if number == 1 or number == 2 or number == 12:
    print("Winter")
elif number >= 3 and number <= 5:
    print("Spring")
elif number >= 6 and number <= 8:
    print("Summer")
elif number >= 9 and number <= 11:
    print("Autumn")
