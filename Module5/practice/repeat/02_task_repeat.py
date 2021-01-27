# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    temp_number = number
    a = 0
    i = 0
    while number > 0:
        a *= 10
        i += 1
        a += number % 10
        number = number // 10
    return temp_number == a


ent_number = int(input('Введи число: '))
print(palindrome(ent_number))
