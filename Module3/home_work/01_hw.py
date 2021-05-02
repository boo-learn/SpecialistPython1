# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

# 1-й вариант
string = ', '.join(names)
print(string)

# 2-й вариант
string = ""
for name in names:
    string += name + ', '
string = string[:-2]
print(string)

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
