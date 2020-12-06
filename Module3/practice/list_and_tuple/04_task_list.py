# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here
input_list = [-1, -5, 1, 2, 3]
pos_sum = 0
for i in input_list:
    if i > 0:
        pos_sum += i
print(pos_sum)
