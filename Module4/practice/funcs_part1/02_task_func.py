# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    reverse = 0
    number_init = number
    while number > 0:
        dig = number % 10
        reverse = reverse * 10 + dig
        number = number // 10
    if reverse == number_init:
        print('Yes')
    else:
        print('No')

# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
