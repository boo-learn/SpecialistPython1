# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    number_of_digits = 0
    while number > 10 ** number_of_digits:
        number_of_digits += 1

    # print  (10 ** number_of_digits - 1)
    first_digit = number // 10 ** (number_of_digits - 1)
    last_digit = number % 10
    other_didits = (number - first_digit * 10 ** (number_of_digits - 1)) // 10
    return (first_digit == last_digit) or (palindrome(other_didits) and (other_didits != 0))

    # Тестируем функцию


print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
