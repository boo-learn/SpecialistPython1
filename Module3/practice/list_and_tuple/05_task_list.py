# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

# Исходные данные:
fruits = ["apple", "banan", "pineapple", "applepen", 'kiwi', 'h', 'j', 'y', 'hg', 'hgd']

max_len = 0
for i, fruit in enumerate(fruits):
    n_len = len(fruit) + len(str(i + 1))
    if n_len > max_len:
        max_len = n_len

for i, fruit in enumerate(fruits):
    spaces = max_len - len(fruit) - len(str(i + 1))
    result = spaces* ' ' + fruit
    print(str(i + 1) + '.', result)

# TODO: your code here

# Пример вывода:
# 1. яблоко
# 2.  банан
# 3.    киви
# 4.  арбуз

# Важно! Ваше решение должно работать с любыми корректными "исходными данными"
# Проверьте это, добавив или удалив несколько элементов списка
