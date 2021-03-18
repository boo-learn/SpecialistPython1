# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("Enter 1st number: "))     # Первое число
second_number = int(input("Enter second number that should be more then 1st: "))    # Второе число

my_list = list(range(first_number, second_number + 1))

for el in my_list:
    if el % 3 == 0:
        print(el)
