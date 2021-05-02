# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
stroka = ''
for i in names:
    if i == names[len(names) - 1]:
        stroka += i
    else:
        stroka += i + ', '
print(stroka)
