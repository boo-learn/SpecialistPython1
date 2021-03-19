# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    temp = number
    number_rev = 0
    while temp > 0:
        number_rev = number_rev * 10 + temp % 10 #take last digit in the original number, place it at the beginning of new one
        temp = temp // 10 #shift the original number to the right
    if number == number_rev:
        return 0 #positve answer - number is palindrome
    else:
        return -1 #negative answer - number is not palindrome

# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
