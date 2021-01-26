# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("Первое число:"))  # Первое число
second_number = int(input("Второе число:"))  # Второе число

my_list = []

if first_number > second_number:
    max_number = first_number
    min_number = second_number
else:
    max_number = second_number
    min_number = first_number

while min_number <= max_number:
    if min_number % 3 == 0 and min_number != 0:
        my_list.append(min_number)
    min_number += 1

print("Список чисел кратных трем:", my_list)
