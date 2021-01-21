# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
names_in_string = ''
for index, name in enumerate(names, 1):
    if index < len(names):
        name += ', '
    names_in_string += name
print(names_in_string)
