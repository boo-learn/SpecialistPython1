# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    initial_number = number
    new_number = 0
    while initial_number > 0:
        new_number *= 10
        new_number += initial_number % 10
        #print(new_number)
        initial_number = initial_number // 10
        #print(initial_number)
    return new_number == number

a = 3
b = 115

list = []
while a<=b:
    list.append(a)
    a += 1

print(list)
for el in list:
    if el//10 >= 1 and palindrome(el):
        print(el)
