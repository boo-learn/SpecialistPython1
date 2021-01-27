# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    temp_number = number
    revers_number = 0
    while (number > 0):
        digit = number % 10
        number = number // 10
        revers_number = revers_number * 10
        revers_number += digit
    if (temp_number == revers_number):
        return "YES"
    return "NO"


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
