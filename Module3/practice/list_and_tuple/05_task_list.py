# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

# Исходные данные:
fruits = ["яблоко", "банан", "киви", "арбуз"]
max_len = 0
curr_len = 0
for fruit in fruits:
    curr_len = len(fruit)
    if curr_len > max_len:
        max_len = curr_len
#
for fruit in fruits:
    delta_len = max_len - len(fruit)
    str_to_print = ' ' * delta_len + fruit
    print(str_to_print)
