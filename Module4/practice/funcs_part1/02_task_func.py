# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    number_x = number
    new_number = 0
    while number_x != 0:
        new_number = new_number * 10 + number_x % 10
        number_x //= 10
    if number == new_number:
        return f'{number} palindrome'
    return f'{number} no palindrome'


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
