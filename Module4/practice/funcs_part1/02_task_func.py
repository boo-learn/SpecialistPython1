# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    number_for_task=number
    revers_number = 0
    while number_for_task > 0:
        n_number = number_for_task%10
        number_for_task = number_for_task//10
        revers_number =revers_number*10
        revers_number += n_number
    #print (revers_number)
    if revers_number==number:
       return "Yes"
    return "No"


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
