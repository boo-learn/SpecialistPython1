# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

new_el = first_number
my_list = [first_number]

while new_el < second_number:
    new_el = new_el + 1
    my_list.append (new_el)
        
print ("My list: ", my_list)

for el in my_list:
    if el % 3 == 0:
        print (el)
