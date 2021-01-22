
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_list = list(str(ticket_number))
    ticket_list = [int(i) for i in ticket_list]  # <- По хорошему тут надо обработку исключения
    return len(ticket_list) == 6 and sum(ticket_list[:3]) == sum(ticket_list[3:])


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436752))
