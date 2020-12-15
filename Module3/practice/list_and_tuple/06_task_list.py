# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
num = first_number

while num <= second_number:
    if num % 3 == 0:
        print(num)
        num += 1
    else:
        num += 1
