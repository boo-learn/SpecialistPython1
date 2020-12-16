# Напишите функцию находящую n-ое число Фибоначчи.
ef fibonacci_n(n):
    first=0
    sekond=1
    i=2
    while i<n:
        i+=1
        next=first+sekond
        first=sekond
        sekond=next
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return next

n=7
print(fibonacci_n(n))
