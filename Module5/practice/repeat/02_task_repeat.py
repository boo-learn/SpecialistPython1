# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    str_num = str(number)
    return True if str_num == str_num[::-1] else False

print(palindrome(2344321))
print(palindrome(2347432))
