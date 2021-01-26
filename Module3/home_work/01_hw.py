# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр

my_string = ''
for n_name in names:
    my_string += n_name + ', '

my_string = my_string[0:-2]
print(my_string)
