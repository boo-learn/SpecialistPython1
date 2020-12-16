# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке
def palindrome(number):
    z = 0
    num = number
    while num // 10 > 0:
        num = num // 10
        z += 1

    buf = 0
    number_ = number
    for i in range(z):
        if number % 10 == number_ // 10**(z-i):
            buf += 1
            number = number // 10
            a = number_ // 10**(z-i)
            number_ = number_ - a*10**(z-i)
        else:
            buf = 0

    if buf > 0:
        return ('YES')
    else:
        return ('NO')
# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
