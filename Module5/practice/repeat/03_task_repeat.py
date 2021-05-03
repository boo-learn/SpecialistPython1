# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    s = str(number)
    return s == s[::-1]


def range_of_palindromes(a, b):
    for i in range(a, b + 1):
        if palindrome(i):
            print(i)


a = 4
b = 10000
range_of_palindromes(a, b)
