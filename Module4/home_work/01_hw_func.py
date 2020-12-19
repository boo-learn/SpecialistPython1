# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

x = lambda z: 'Yes' if ( z[ :(len(z)//2) ] == z[:(len(z)//2)-1:-1]) else 'No'

def lucky_ticket(ticket_number):
    return x(str(ticket_number))
print(lucky_ticket(123456789987654321))


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
