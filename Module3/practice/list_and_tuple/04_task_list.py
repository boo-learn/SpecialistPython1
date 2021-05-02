# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here

numbers = [-6, 2, 5, 0, -4, 6, 8]
sum_of_numbers = 0
for number in numbers:
    if number>=0:
        sum_of_numbers+=number
print(sum_of_numbers)
