# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

# a = ...
# b = ...

a = 1
b = 200

def palindrome(number):
    return str(number) == str(number)[::-1]

def count_palindrome(a, b):
    total = 0
    for i in range(a, b + 1):
        total += palindrome(i)
    return total
print(count_palindrome(a, b))
