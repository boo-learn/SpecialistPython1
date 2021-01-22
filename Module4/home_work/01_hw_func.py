# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def revers_number(number): #
    revers_num = 0
    while number != 0:
        revers_num += number % 10
        number = number // 10
        if number != 0:
            revers_num *= 10
    return revers_num
#print(revers_number(12348768875678900005))

def sum_two_last(number):
    return number % 10 + number // 10 % 10


def lucky_ticket(ticket_number):

    return sum_two_last(ticket_number) == sum_two_last(revers_number(ticket_number))


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
