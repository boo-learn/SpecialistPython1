# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    return str(number) == str(number)[::-1]


def pal_count(a, b):
    count = 0
    for number in range(a, b + 1):
        if palindrome(number):
            count += count
    return count
