# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

my_list = [10, 3, -4, -9, 2, 3, 1, 10, 8, 2]
sum_elements = 0
for element in my_list:
    if element > 0:
        sum_elements += element
print(sum_elements)
