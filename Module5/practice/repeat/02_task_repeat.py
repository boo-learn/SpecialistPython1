# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    revers = 0
    number2 = number
    while True:
        digit = number % 10
        number = number // 10
        revers = revers * 10 + digit
        if number == 0:
            break
    return number2 == revers

print(palindrome(12321))
print(palindrome(1231))
