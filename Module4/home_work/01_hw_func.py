# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    s = str (ticket_number)
    return True if (int(s[0]) + int(s[1]) + int(s[2]) == int(s[3]) + int(s[4]) + int(s[5])) else False


print(lucky_ticket(123006))
print(lucky_ticket(123210))
print(lucky_ticket(436751))


# Тестируем функцию
print(lucky_ticket(123006))
#print(lucky_ticket(12321)) 5-значный номер
print(lucky_ticket(436751))
