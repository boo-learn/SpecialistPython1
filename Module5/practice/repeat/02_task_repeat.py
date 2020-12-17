# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    revers=0
    num=number
    while number:
        revers=revers*10+number%10
        number//=10
    return revers==num

print(palindrome(12321))
