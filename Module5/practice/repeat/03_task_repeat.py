# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    num = number
    revers_num = 0
    while num != 0:
        revers_num += num % 10
        num = num // 10
        if num != 0:
            revers_num *= 10
    return revers_num == number

a = 1
b = 10
quantity = 0
for i in range(a,b+1):
    if palindrome(i):
        quantity +=1
print(quantity)
