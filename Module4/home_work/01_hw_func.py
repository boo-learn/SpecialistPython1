# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def sum_of_digits(number):
    s=0
    while number>0:
        s+=number%10
        number//=10
    return s


def lucky_ticket(ticket_number):
    left_part=ticket_number//1000
    right_part=ticket_number%1000
    return sum_of_digits(left_part)==sum_of_digits(right_part)


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
