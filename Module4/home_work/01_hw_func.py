# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    parts = list(divmod(ticket_number, 1000))
    for i in range(2):
        s = 0
        while parts[i] > 0:
            s += parts[i] % 10
            parts[i] //= 10
        parts[i] = s
    if parts[0] == parts[1]:
        return 'YES'
    else:
        return 'NO'
    
def summa(*args):
    s = 0
    for arg in (args):
        s += arg
    return s


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
