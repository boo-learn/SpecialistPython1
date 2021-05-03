# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def quantity_palindrome(a,b):
    i = 0
    palind_numbers = 0
    while i < (b-a):
        number = b- i
        if str(number) == str(number)[::-1]:
            palind_numbers += 1
        i+=1
    return palind_numbers
