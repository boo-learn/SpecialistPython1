# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    n = number
    revers = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        revers = revers * 10 + digit
    if number == revers:
        return (True)
    return (False)

print(palindrome(3454))
print(palindrome(3663))
