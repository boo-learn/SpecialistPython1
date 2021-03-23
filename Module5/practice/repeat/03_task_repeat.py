# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.
def palindrome(number):
    n = number
    revers = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        revers = revers * 10 + digit
    if number == revers:
        return (True)
    return (False)

a= 50
b = 67
el= a
qty = 0
while el<=b:
    if palindrome(el):
        qty = qty +1
    el = el +1
print (qty)
