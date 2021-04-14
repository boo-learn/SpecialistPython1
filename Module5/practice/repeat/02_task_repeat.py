# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def num_palindrome(number):
    straight = number
    reverse = 0
    while straight > 0:
        reverse = reverse * 10 + straight % 10
        straight //= 10
    return reverse == number
