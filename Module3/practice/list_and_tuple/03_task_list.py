# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

my_list = [10, 3, -4, -9, 2, 3, 1, 0 , 8, 2]
sum_elements = 0
for new_list in my_list:
    sum_elements += new_list
print(sum_elements)
