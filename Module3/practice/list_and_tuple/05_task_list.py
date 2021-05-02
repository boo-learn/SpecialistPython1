# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

# Исходные данные:
fruits = ["яблоко", "банан", "киви", "арбуз"]

max_len = 0
for fruit in fruits:
    if len(fruit) > max_len:
        max_len = len(fruit)
length_of_last_index_of_array = len(str(len(fruits)))
for i, fruit in enumerate(fruits, 1):
    number_of_spaces = max_len - len(fruit) + length_of_last_index_of_array - len(str(i)) + 1
    spaces = ""
    j = 0
    while j < number_of_spaces:
        spaces += " "
        j += 1
    print(str(i) + "." + spaces + fruit)

# Пример вывода:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Важно! Ваше решение должно работать с любыми корректными "исходными данными"
# Проверьте это, добавив или удалив несколько элементов списка
