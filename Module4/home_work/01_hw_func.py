# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    if ticket_number // 10**5 == 0:
        return ('Некорректный номер билета')
    else:
        str_num = str(ticket_number)
        lft_sum = sum(map(int,str_num[:4]))
        rgt_sum = sum(map(int,str_num[4:]))
        
        return lft_sum == rgt_sum 
# Или так:

def lucky_ticket(ticket_number):
    if ticket_number // 10**5 == 0:
        return ('Некорректный номер билета')
    else:
        lft_num = tuple(str(ticket_number // 10**3))
        rgt_num = tuple(str(ticket_number % 10**3))
        
        lft_sum = sum(tuple(map(lambda x: int(x), lft_num)))
        rgt_sum = sum(tuple(map(lambda x: int(x), rgt_num)))
        
        return lft_sum == rgt_sum     
    
# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
