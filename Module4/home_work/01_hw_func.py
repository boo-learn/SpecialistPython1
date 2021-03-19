# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

ll = []
rr = []


def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    if len(ticket_number) != 6:
        print(f"ticket_number:{ticket_number} has not 6 digits")
        return 1

    left = ticket_number[:-3]
    for el in left:
        el = int(el)
        ll.append(el)

    left_sum = sum(ll)

    right = ticket_number[-3:]
    for el2 in right:
        el2 = int(el2)
        rr.append(el2)

    right_sum = sum(rr)

    if left_sum == right_sum:
        print(f"ticket number:{ticket_number} is lucky ticket!")
    else:
        print(f"ticket number:{ticket_number} is NOT lucky ticket!")

    return ticket_number


lucky_ticket(123006)
lucky_ticket(12321)
lucky_ticket(436751)
