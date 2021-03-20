# Напишите функцию находящую n-ое число Фибоначчи.
def fib(n):
    if n < 0:
        return
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# test
n = [-1, 0, 10, 15]
for el in n:
    res = fib(el)
    print(f"for n={el}, Fib={res}")
