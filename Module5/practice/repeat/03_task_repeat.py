# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    return str(number) == str(number)[::-1]

a = 0
b = 10000

for i in range (a,b+1):
    if palindrome(i): print(i)
