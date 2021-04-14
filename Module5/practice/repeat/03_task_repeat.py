# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    return str(number) == str(number)[::-1]


a = 10
b = 50
count = 0
while a <= b:
    if palindrome(a): count += 1
    a += 1
print(count)
