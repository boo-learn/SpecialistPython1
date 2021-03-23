# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

a = 11
b = 33


def palindrome(number):
    return str(number) == str(number)[::-1]


count = 0
for num in range(a, b + 1):
    if palindrome(num):
        count += 1

print(count)
