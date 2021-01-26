# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
list = []
big = 0
small = 0
if first_number > second_number:
    big = first_number
    small = second_number
else:
    small = first_number
    big = second_number

while small <= big:
    list.append(small)
    small += 1

for el in list:
    if el%3 == 0:
        print(el)
