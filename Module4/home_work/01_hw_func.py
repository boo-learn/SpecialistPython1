# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_number_str = str(ticket_number)
    if len(ticket_number_str) != 6:
        return False
    sum_beg = 0
    sum_end = 0
    for i in range(3):
        sum_beg += int(ticket_number_str[i])
        sum_end += int(ticket_number_str[i + 3])
    return sum_beg == sum_end


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
