# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    number = str(number)
    _palindrome = number[::-1]

    return _palindrome == number

number = 12342
if palindrome(number):
    pass
