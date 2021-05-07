# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("Введите первое число: "))  # Первое число
second_number = int(input("Введите второе число: "))  # Второе число
if first_number > second_number:
    first_number, second_number = second_number, first_number
list_numbers = []

for i in range(first_number, second_number):
    if i % 3 == 0:
        list_numbers.append(i)
print(list_numbers)
