# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
first_number = int(input())
second_number = int(input())

if first_number > second_number:
    less = second_number
    more = first_number
else:
    more = second_number
    less = first_number

i = less
while i <= more:
    if i % 3 == 0:
        print(i)
    i +=1;
