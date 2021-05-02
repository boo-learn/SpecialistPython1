# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
numbers = [-26, -23, -61, 22, 72, -4, 34, 24, -24, 70, -35, 28, -14, -38, -50]
summ = 0
for number in numbers:
    if number % 2 == 0 and number > 0:
        # print(number)
        summ += number
print(summ)
