# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр

if 0:
    str_name = ''
    for name in names:
        str_name += name + ','
    print(str_name[:len(str_name)-1])

#============================
if 1:
    lng_names = len(names)
    str_name = ''
    num = 0
    while num < lng_names-1:
        str_name += names[num] + ','
        num += 1
    str_name += names[num]

    print(str_name)
#============================
if 0:
    sjoin = ','.join(names)
    print(sjoin)

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
