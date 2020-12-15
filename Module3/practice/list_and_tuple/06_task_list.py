# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

lst = list()
i = min(first_number,second_number)
while i <= max(first_number,second_number):
    if i % 3 == 0:
        lst.append(i)
    i += 1

print(lst)
