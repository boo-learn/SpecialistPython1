# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    copy_number = number
    reverse_number = 0
    while number > 0:
        reverse_number += number % 10
        number //= 10
        if number > 0:
            reverse_number *= 10
    print(reverse_number)
    if reverse_number == copy_number:
        return True
    return False
        


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
