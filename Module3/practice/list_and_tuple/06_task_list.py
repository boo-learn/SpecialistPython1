# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input("Введите первое число: "))     # Первое число
second_number = int(input("Введите второе число: "))    # Второе число
i=first_number-1
count=0
while i< second_number:
    i+=1
    if i%3==0:
        count+=1
print(count)
# TODO: your code here
