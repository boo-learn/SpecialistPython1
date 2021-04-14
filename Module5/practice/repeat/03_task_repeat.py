# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

a = ...
b = ...

def num_palindrome(number):
    straight = number
    reverse = 0
    while straight > 0:
        reverse = reverse * 10 + straight % 10
        straight //= 10
        #print(straight, reversed)
    return reverse == number

def find_palindromes(a, b):
    res = []
    for i in range(a, b+1):
        if num_palindrome(i):
            res.append(i)
    return res # len(res)
