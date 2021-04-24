# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# TODO: your code here
m = int(input("put the month please: "))
if m==12 or m==1 or m==2:
    print("winter")
elif m==3 or m==4 or m==5:
    print("spring")
elif m==6 or m==7 or m==8:
    print("summer")
elif m==9 or m==10 or m==11:
    print("осень")
