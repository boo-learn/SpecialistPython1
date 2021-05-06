# Напишите функцию находящую n-ое число Фибоначчи.

def fibonacci(n):
    n1 = 0
    n2 = 1
    for _ in range(n):
        res = n1 + n2
        n1 = n2
        n2 = res
    return n1


print(fibonacci(1000000))
