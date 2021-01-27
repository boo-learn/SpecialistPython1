# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):

    first_dig = number
    while first_dig//10 !=0:
        first_dig = first_dig//10

    last_dig = number%10

    if first_dig == last_dig:
        return "палиндромом"
    return "не палиндромом"


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
