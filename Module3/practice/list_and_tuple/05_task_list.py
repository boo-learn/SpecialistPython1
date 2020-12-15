# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне - слева короткие слова дополняем символами пробела

fruits = ["яблоко", "банан", "киви", "арбуз"]
sort_fruits=fruits
sort_fruits.sort(key=len,reverse=True) #key=len,reverse=True
max_len=len(sort_fruits[0])
print(fruits)
print(sort_fruits)
print(max_len)
for i, fruit in enumerate(fruits,1):
    print(i," "," "*(max_len-len(fruit)), fruit)

# Пример вывода:
# 1. яблоко
# 2.  банан
# 3.    киви
# 4.  арбуз

# Важно! Ваше решение должно работать с любыми корректными "исходными данными"
# Проверьте это, добавив или удалив несколько элементов списка
