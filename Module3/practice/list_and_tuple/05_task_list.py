# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

# Исходные данные:
fruits = ["яблоко", "банан", "киви", "арбуз"]
max_len = 0
i = 1

for fruit in fruits:
    len_fruit = len(fruit)
    if len_fruit > max_len:
        max_len = len_fruit

for fruit in (fruits):
    symb = max_len - len(fruit)
    print(i,(" ")*symb,fruit)
    i += 1
