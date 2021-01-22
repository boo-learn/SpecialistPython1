# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    return str(number) == str(number)[::-1]


def count_palindrome(lim_down, lim_up):
    count = 0
    for num in range(lim_down, lim_up):
        if palindrome(num):
            count += 1
    return count


a = 10
b = 100
print(count_palindrome(a, b))
