# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    digits = [int(x) for x in str(number)]
    is_palindrome, i = True, 0
    for i in range(int(len(digits)/2)):
        is_palindrome = is_palindrome and digits[i] == digits[-i-1]
    return is_palindrome

# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
