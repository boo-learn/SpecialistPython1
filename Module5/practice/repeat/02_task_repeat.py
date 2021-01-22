# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    num = number
    revers_num = 0
    while num != 0:
        revers_num += num % 10
        num = num // 10
        if num != 0:
            revers_num *= 10
    return revers_num == number
