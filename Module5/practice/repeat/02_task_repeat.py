# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    copy_num = number
    reverse_num = 0
    while number > 0:
        reverse_num += number % 10
        number //= 10
        if number > 0:
            reverse_num *= 10
    return reverse_num == copy_num
    
print(palindrome(12321))
