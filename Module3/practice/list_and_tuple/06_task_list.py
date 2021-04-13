# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
i = first_number
res_list = []
while i <= second_number:
    if i % 3 == 0:
        res_list.append(i)
    i += 1
    
print(res_list)
