# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

divide_on_three = []
for num in range(first_number, second_number + 1):
    if num%3 == 0:
        divide_on_three.append(num)

print(divide_on_three)
