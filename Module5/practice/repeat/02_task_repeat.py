# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    number = str(number)
    palindrome = number[::-1]

    return palindrome == number


print(palindrome(12321))
print(palindrome(123456))
print(palindrome(12344))
