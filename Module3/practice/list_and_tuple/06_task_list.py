# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число
num = first_number
list_to_print = []
while num <= second_number:
    if num % 3 == 0:
        list_to_print.append(num)
    num += 1
print(list_to_print)
