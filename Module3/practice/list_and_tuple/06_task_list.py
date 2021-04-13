# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

lst = []

a = first_number
b = second_number

if first_number > second_number:
    while b <= a:
        if b % 3 == 0:
            lst.append(b)
        b += 1
else:
    while a <= b:
        if a % 3 == 0:
            lst.append(a)
        a += 1
print (lst)
