# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def rev(number):
    rev_n = 0
    copy_n = number
    while copy_n:
        rev_n = 10 * rev_n + copy_n % 10
        copy_n = copy_n // 10
    return rev_n


def lucky_ticket(ticket_number):
    rev_ticket_number = rev(ticket_number)
    left_half = 0
    right_half = 0
    for c in range(len(str(ticket_number)) // 2):
        left_half = left_half + ticket_number % 10
        ticket_number = ticket_number // 10
        right_half = right_half + rev_ticket_number % 10
        rev_ticket_number = rev_ticket_number // 10
    return bool(left_half == right_half)


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
