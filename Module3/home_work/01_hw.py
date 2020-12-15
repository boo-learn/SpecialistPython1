# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
if 0:  # ВАРИАНТ 1. Работает
    str_to_print = ''
    for name in names:
        str_to_print += name
        str_to_print += ', '
    print(str_to_print[:-2])
if 0:  # ВАРИАНТ 2. этот вариант усекает список в цикле
    str_to_print = ''
    names.reverse()
    while names:
        str_to_print += names.pop()
        str_to_print += ', '
    print(str_to_print[:-2])
if 1:  # ВАРИАНТ 3. использует str.join
    delim = ', '
    print(delim.join(names))
# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
