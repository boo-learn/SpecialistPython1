# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    temp = number
    number_rev = 0
    while temp > 0:
        number_rev = number_rev * 10 + temp % 10 #take last digit in the original number, place it at the beginning of new one
        temp = temp // 10 #shift the original number to the right
    return number == number_rev

print(palindrome(12321))
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
