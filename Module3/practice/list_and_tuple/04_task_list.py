# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
my_list = [-1, 2, 5, -3]

sum_positive_els = 0

for el in my_list:
    if el > 0:
        sum_positive_els += el
print(sum_positive_els)
