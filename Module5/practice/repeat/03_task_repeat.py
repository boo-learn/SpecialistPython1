# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    return True if str(number) == str(number)[::-1] else False

def palin_count(a, b):
    count = 0
    for _ in range(a, b):
        if palindrome(_):
            count += 1
    return count

print(palin_count(10, 34))
