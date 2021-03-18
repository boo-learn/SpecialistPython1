# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

# Исходные данные:
# fruits = ["яблоко", "банан", "киви", "арбуз"]

# Пример вывода:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Важно! Ваше решение должно работать с любыми корректными "исходными данными"
# Проверьте это, добавив или удалив несколько элементов списка

fruits = ["яблоко", "банан", "киви", "арбуз"]

max_len = len(max(fruits, key=len))

j = 1

for el in fruits:
    new_str = str(j) + ". "
    spaces = max_len - len (el)
    i = 0
    while i < spaces:
        new_str = new_str + " "
        i += 1
    new_str = new_str + el   
    print (new_str)
    j += 1
