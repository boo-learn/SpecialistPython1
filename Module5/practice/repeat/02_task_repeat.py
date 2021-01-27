# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    temp_number = number
    revers_number = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        revers_number = revers_number * 10
        revers_number += digit
    return temp_number == revers_number
