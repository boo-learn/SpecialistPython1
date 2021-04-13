# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
list_3 = []
for i in range(first_number + 1, second_number):
    if i % 3 == 0:
        list_3.append(i)

print(list_3)
