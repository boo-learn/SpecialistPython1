# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    string = str(number)
    rev_string = string[::-1]
    # print(string == rev_string)
    return string == rev_string

palindrome(12321)
