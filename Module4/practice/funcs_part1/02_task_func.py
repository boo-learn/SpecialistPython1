# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке
def palindrome(number):
    st=str(number)
    rev_st = st [::-1]
    rev_number = int(rev_st)
    if rev_number == number:
        return ('yes')
    return('no')


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
