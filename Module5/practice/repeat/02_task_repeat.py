# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    # return str(number) == str(number)[::-1]
    rev_number = 0
    copy_number = number
    while copy_number:
        rev_number = 10 * rev_number + copy_number % 10
        copy_number = copy_number // 10
    return rev_number == number


n = int(input("Введите число: "))
if palindrome(n):
    print("Число палиндром")
else:
    print("Число не палиндром")
