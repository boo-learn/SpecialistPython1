# Напишите функцию находящую n-ое число Фибоначчи.
def fibonacci(n):
    fib0 = 0
    fib1 = 1
    for _ in range(n):
        fib0 = fib1
        fib1 += fib0
    return fib0

for i in range(10):
    print(fibonacci(i))
