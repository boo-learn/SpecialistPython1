# Напишите функцию находящую n-ое число Фибоначчи.
def fib_num(n):
    fib0 = 0
    fib1 = fib2 = 1
    i = 0
    while i < n - 3:
        fib = fib0 + fib1 + fib2
        fib1 = fib2
        fib2 = fib
        i += 1
    return (fib)

print(fib_num(7))
