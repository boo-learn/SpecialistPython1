# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

# TODO: your code here

numbers = [10, -2, -1, 5, 9, 4, -3]
sum_of_numbers = 0
for number in numbers:
    if number > 0:
        sum_of_numbers += number
print(sum_of_numbers)
